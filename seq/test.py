from loki import *
src_file = "sub.F90"
src_name = "TEST"
source = Sourcefile.from_file(src_file)
routine = source[src_name]

routine.spec.insert(0,ir.Pragma(keyword='acc', content='routine ('+    routine.name+') seq'))
routine.spec.insert(1,ir.Comment(text=''))

print(fgen(routine))
