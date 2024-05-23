code="""SUBROUTINE SUB(A,B,KLON,KLEV)

IMPLICIT NONE

REAL (KIND=JPRB), INTENT(INOUT) :: A
REAL (KIND=JPRB), INTENT(INOUT) :: B
INTEGER, INTENT(IN) :: KLON
INTEGER, INTENT(IN) :: KLEV

#ifdef COND
DO JLEV=1,KLEV
DO JLON=KIDIA,KFDIA
#else
DO JLON=KIDIA,KFDIA
DO JLEV=1,KLEV
#endif 
A(JLON,JLEV)=B(JLON,JLEV)+1
ENDDO
ENDDO

END SUBROUTINE
"""


from loki import *
source=Sourcefile.from_source(code, True, defines=['COND'])
sub=source["SUB"]
print(fgen(sub))
