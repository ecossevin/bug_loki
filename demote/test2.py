from loki import *
src_file = "sub2.F90"
src_name = "ACDNSHF_OPENACC"
source = Sourcefile.from_file(src_file)
routine = source[src_name]

var_names=('ZZPN', 'ZZDRCN', 'ZZDLLS', 'ZZDLLW', 'ZZDLS')
horizontal_size='KLON'
demote_variables(routine, var_names, dimensions=horizontal_size)

print(fgen(routine))
