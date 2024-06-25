from loki import *
import sys


file_name = "apl_arpege_parallel.F90"
#file_name = "sub.F90"
source=Sourcefile.from_file(file_name)
src_name = "APL_ARPEGE_PARALLEL"
#src_name = "TOTO"
routine=source[src_name]
sanitise_imports
print(fgen(routine))
