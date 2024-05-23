from loki import (
    Sourcefile, FindNodes, CallStatement, 
    Transformer, Dimension, ir, 
    Scalar, Assignment, fgen,
    FindVariables, symbols, demote_variables,
    Intrinsic, Variable, SymbolAttributes,
    DerivedType, VariableDeclaration, flatten,
    BasicType, SubstituteExpressions,
    FindExpressions, FindInlineCalls
)

from loki.transform import inline_member_procedures

from loki import analyse_dataflow

file="present.F90"
source=Sourcefile.from_file(file, preprocess=False)
#source=Sourcefile.from_file(file, preprocess=True)
routine=source["CALLER"]

print(routine.members)
#routine.enrich_calls(routine.members)
inline_member_procedures(routine)

print("*************** INLINE ECMWF ***************")
print(fgen(routine))
