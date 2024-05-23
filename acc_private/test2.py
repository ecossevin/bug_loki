from loki import *
import sys
path_irgrip="/home/cossevine/kilo/src/acdc/loki"
sys.path.append(path_irgrip)
import irgrip
path="sub.F90"
private="JLON, YLCPG_BNDS, YLSTACK, JLON, YLCPG_BNDS, YLSTACK, JLON, YLCPG_BNDS, YLSTACK, JLON, YLCPG_BNDS, YLSTACK, JLON, YLCPG_BNDS, YLSTACK, JLON, YLCPG_BNDS, YLSTACK, JLON, YLCPG_BNDS, YLSTACK, JLON, YLCPG_BNDS, YLSTACK"
#private="JLON, YLCPG_BNDS, YLSTACK"
code=f"""
     !$ACC LOOP VECTOR &\n
     !$ACC PRIVATE ({private})\n"""
code=f"!$ACC LOOP VECTOR  PRIVATE ({private})\n"
ccode=irgrip.slurp_any_code(code)
print(code)
print(ccode)
print(fgen(ccode))

