
import os
import numpy as np
from matplotlib import pyplot as plt

results = []

for d, dn, fn in os.walk("."):
    for dir in sorted(dn):
        if "scf-" in dir:
            try:
                E = 0
                with open(d+"/"+dir+"/scf.out") as f:
                    for line in f:
                        if "!" in line:
                             E = float(line.split()[4])
                results.append([float(dir.split("-")[1]), float(dir.split("-")[2]), E])
            except:
                pass

for i in range(len(results)):
    for j in range(len(results)):
        X[i,j] = 
plt.plot_wireframe(
