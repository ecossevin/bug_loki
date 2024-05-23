from loki import *
path="sub.F90"
file=Sourcefile.from_file(path)
routine=file["TOTO"]
print(routine.body.body)
print(fgen(routine))

