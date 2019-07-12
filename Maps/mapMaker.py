import numpy as np

from random import *

for n in range(50):
	mat = []
	for x in range(101):
		mat.append([])
		for y in range(101):
			if (random() < 0.7):
				mat[x].append(0)
			else:
				mat[x].append(1)

	filename = 'map' + str(n) + '.txt'
	np.savetxt(filename, mat, delimiter=",", newline = "\n", fmt='%i')