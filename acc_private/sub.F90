SUBROUTINE TOTO(A,B)

IMPLICIT NONE
REAL, INTENT(IN) :: A
REAL, INTENT(INOUT) :: B

!$ACC LOOP VECTOR &
!$ACC&PRIVATE( JBLK, JLON, YLCPG_BNDS, YLSTACK )


END SUBROUTINE TOTO
