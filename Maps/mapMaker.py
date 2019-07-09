import numpy as np

from random import *
from util import *

for n in range(DIM):
	mat = []
	for x in range(DIM):
		mat.append([])
		for y in range(DIM):
			if (random() < 0.7):
				mat[x].append(0)
			else:
				mat[x].append(1)

	mat[0][0] = 2
	mat[100][100] = 3

	filename = 'map' + str(n) + '.txt'
	np.savetxt(filename, mat, delimiter=",", newline = "\n", fmt='%i')