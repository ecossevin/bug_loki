from loki import * 

fcode1 = """
    SUBROUTINE TEST

    !$loki parallel TARGET=OpenMP/OpenMPSingleColumn/OpenACCSingleColumn,NAME=CPPHINP 
    PRINT *, "loki"
    !$loki end parallel

    END SUBROUTINE"""


routine = Sourcefile.from_source(fcode1)["TEST"]
with pragma_regions_attached(routine):
    for region in FindNodes(PragmaRegion).visit(routine.body):
        print(f"{region=}")
        print("region = ", fgen(region.body))
        assert fgen(region.body) == 'PRINT *, "loki"'

fcode2 = """
    SUBROUTINE TEST

    !$ACDC PARALLEL TARGET=OpenMP/OpenMPSingleColumn/OpenACCSingleColumn,NAME=CPPHINP 
    PRINT *, "ACDC_endparallel"
    !$ACDC END PARALLEL


    END SUBROUTINE"""

routine = Sourcefile.from_source(fcode2)["TEST"]
with pragma_regions_attached(routine):
    for region in FindNodes(PragmaRegion).visit(routine.body):
        print(f"{region=}")
        print("region = ", fgen(region.body))
        assert fgen(region.body) == 'PRINT *, "ACDC_endparallel"'

fcode3 = """
    SUBROUTINE TEST

    !$ACDC PARALLEL,TARGET=OpenMP/OpenMPSingleColumn/OpenACCSingleColumn,NAME=CPPHINP 
    PRINT *, "ACDC_coma"
    !$ACDC END PARALLEL


    END SUBROUTINE"""
routine = Sourcefile.from_source(fcode3)["TEST"]
with pragma_regions_attached(routine):
    for region in FindNodes(PragmaRegion).visit(routine.body):
        print(f"{region=}")
        print("region = ", fgen(region.body))
        assert fgen(region.body) == 'PRINT *, "ACDC_coma"'

fcode4 = """
    SUBROUTINE TEST

    !$ACDC PARALLEL TARGET=OpenMP/OpenMPSingleColumn/OpenACCSingleColumn,NAME=CPPHINP 
    PRINT *, "ACDC_curly_brace"
    !$ACDC }


    END SUBROUTINE"""
routine = Sourcefile.from_source(fcode4)["TEST"]
with pragma_regions_attached(routine):
    for region in FindNodes(PragmaRegion).visit(routine.body):
        print(f"{region=}")
        print("region = ", fgen(region.body))
        assert fgen(region.body) == 'PRINT *, "ACDC_curly_brace"'
