from loki import *
#src_file = "sub.F90"
#src_name = "TEST"
src_file = "ppwetpoint.F90"
src_name = "PPWETPOINT"

source = Sourcefile.from_file(src_file)
routine = source[src_name]

var_lst=FindVariables(unique=True).visit(routine.spec)
for var in var_lst:
    if var.name=="JLON":
        is_present=True
        loop_index=var


lst_horizontal_idx=['JLON','JROF']
rename_map={}
for var in FindVariables().visit(routine.body):
    if var.name in lst_horizontal_idx:
        rename_map[var]=loop_index
routine.body=SubstituteExpressions(rename_map).visit(routine.body)

routine.body = SubstituteExpressions(rename_map).visit(routine.body)

print(fgen(routine.body))
