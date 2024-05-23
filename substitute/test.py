from loki import *
#src_file = "sub.F90"
#src_name = "TEST"
src_file = "ppwetpoint.F90"
src_name = "PPWETPOINT"

source = Sourcefile.from_file(src_file)
routine = source[src_name]

loop_index = routine.variable_map['JLON']
variables = [var for var in FindVariables(unique=True).visit(routine.spec)]
for var in variables:
    if var.name == 'JLON':
        loop_index2 = var

variables = [var for var in FindVariables().visit(routine.body)]
for var in variables:
    if var.name == 'JLON':
        loop_index3 = var

print("test =", loop_index is loop_index2)
print("test =", loop_index is loop_index3)
print("test =", loop_index2 is loop_index3)

rename_map = {loop_index3 : loop_index2}

routine.body = SubstituteExpressions(rename_map).visit(routine.body)

print(fgen(routine.body))
