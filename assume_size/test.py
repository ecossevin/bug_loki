from loki import *
import sys


file_name = "sub.F90"
source=Sourcefile.from_file(file_name)
src_name = "TOTO"
routine=source[src_name]
print(fgen(routine))
