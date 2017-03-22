#!/usr/bin/env python

import sys
import numpy as np
from matplotlib import pyplot as plt

E, N = np.loadtxt(sys.argv[1], usecols = (0,1), unpack = True)

plt.plot(E, N)
plt.savefig(sys.argv[1].replace("dos","png"))
