from loki import Sourcefile
from loki import fgen
from loki import resolve_associates
import logical
import sys
print(len(sys.argv))
print(len(sys.argv))

true_symbols = []
false_symbols = ['LHOOK']

#file_name = "ppwetpoint_bug_test.F90"
file_name = "ppwetpoint_no_bug.F90"
#file_name = "ppwetpoint_bug.F90"
source=Sourcefile.from_file(file_name)
src_name = "PPWETPOINT"
routine=source[src_name]
resolve_associates(routine)
routine_t1 = routine.clone()
