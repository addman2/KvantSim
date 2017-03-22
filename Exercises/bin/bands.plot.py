#!/usr/bin/env python

import sys
import os
import numpy as np
from matplotlib import pyplot as plt

bands = []

with open(os.getcwd()+"/"+sys.argv[1]) as f:
    for i, line in enumerate(f):
        if i%2 == 0:
            try:
                d = np.array(line.split(), np.float)
                bands.append(d)
            except:
                pass
            
bands = np.array(bands)

for b in bands.T:
    plt.plot(b, "b-", linewidth=2)

plt.savefig(sys.argv[1].replace("bands","png"))
