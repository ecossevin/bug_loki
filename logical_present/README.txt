LDFLAG is present when calling the callee. The caller should print "PRESENT" instead of "NOT PRESENT". 

I fixed this by changing in transform_inline.py : 

check: sym.Literal('.true.') if check.arguments[0].name in name_arg_map else sym.Literal('.false.')
#check: sym.Literal('.true.') if check.arguments[0] in call.arg_map else sym.Literal('.false.')

where name_arg_map=[arg.name for arg in call.arg_map]

