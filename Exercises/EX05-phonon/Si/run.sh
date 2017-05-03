
PARA_PREFIX="mpirun -np 6"
NOPA_PREFIX=""

$PARA_PREFIX pw.x     < si.scf.in > si.scf.out
$PARA_PREFIX ph.x     < si.ph.in  > si.ph.out
$NOPA_PREFIX dynmat.x < si.dm.in  > si.dm.out
