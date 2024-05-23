from loki import *
path="sub.F90"
file=Sourcefile.from_file(path)
routine=file["TOTO"]
print(fgen(routine))

