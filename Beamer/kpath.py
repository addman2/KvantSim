from   ase.io import read
from   ase.dft.kpoints  import ibz_points
from   ase.dft.kpoints  import get_bandpath

xtal = read("POSCAR")

ip = ibz_points["cubic"]
points = [ "Gamma", "X", "M", "Gamma"]
path = [ip[p] for p in points]
print(xtal.cell)
kpts, x, X = get_bandpath(path, 
                          xtal.cell, 
                          npoints = 200)

print(kpts)
print(x)
print(X)
