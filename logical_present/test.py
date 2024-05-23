from loki import * 


file="sub.F90"
source=Sourcefile.from_file(file, preprocess=False)
#source=Sourcefile.from_file(file, preprocess=True)
routine=source["CALLER"]

#routine.enrich_calls(routine.members)
inline_member_procedures(routine)

print(fgen(routine))
