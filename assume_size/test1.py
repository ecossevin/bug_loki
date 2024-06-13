#from loki import Sourcefile
#from loki import fgen
#from loki import resolve_associates
from loki import *
import sys


file_name = "sub.F90"
source=Sourcefile.from_file(file_name)
src_name = "TOTO"
routine=source[src_name]
#variables=[var for var in FindVariables().visit(routine.body)]
#variables=[var for var in FindVariables().visit(routine.spec)]
print(fgen(routine))
