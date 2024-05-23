from loki.expression import symbols as sym
from loki.ir import (
    is_loki_pragma, get_pragma_parameters, pragma_regions_attached,
    FindNodes, nodes as ir
)
from loki.transform import Transformation
from loki import (
    FindVariables, DerivedType, SymbolAttributes,
    Array, single_variable_declaration, Transformer,
    BasicType, as_tuple, parse_expr
)
from loki import Sourcefile
import pickle
import os
from itertools import chain
from loki import fgen


from pathlib import Path

def process_ubound(src_file, src_name):
    field_new = []
    source = Sourcefile.from_file(src_file)
    routine = source[src_name]
    for k in range(1):
        temp_arrays = [var for var in FindVariables(Array).visit(routine.spec) if var.name=="ZRDG_MU0"]
        var = temp_arrays[0]
        var_shape = var.shape
    
        dim = len(var_shape) + 1 # Temporary dimensions + block
    
        # The FIELD_{d}RB variable
        field_ptr_type = SymbolAttributes(
            dtype=DerivedType(f'FIELD_{dim}RB'),
            pointer=True, polymorphic=True, initial="NULL()"
        )
        field_ptr_var = sym.Variable(name=f'YL_{var.name}', type=field_ptr_type, scope=routine)
    
        # Create a pointer instead of the array
        shape = (sym.RangeIndex((None, None)),) * dim
##        var.type = var_type.clone(pointer=True, shape=shape)
        local_ptr_var = var.clone(dimensions=shape)

    
        ubounds = [d.upper if isinstance(d, sym.RangeIndex) else d for d in var_shape]
        ubounds += [sym.Variable(name="KGPBLKS", parent=routine.variable_map["YDCPG_OPTS"])]
        kwarguments = (
            ('UBOUNDS', sym.LiteralList(ubounds)),
            #('PERSISTENT', sym.LogicLiteral(True)),
        )
        field_new += [ir.CallStatement(
            name=sym.Variable(name='FIELD_NEW', scope=routine),
            arguments=(field_ptr_var,),
            kwarguments=kwarguments
        )]
        print(fgen(field_new[k]))
        print(f"{hash(field_new[k])=}")
    return(field_new)

src_file = "sub.F90"
src_name = "DISPATCH_ROUTINE"
field_new = process_ubound(src_file, src_name)


