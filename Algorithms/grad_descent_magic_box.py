# Create a magic box of 4x4 where the numbers
# of each row, col, and diag gives the sum of -2

# Solved using cost function with gradient descent


import math
import random

def distance(m):
	sum_distance = 0

	sum_distance += math.fabs(m[0] + m[1] + m[2] + m[3] - -2)
	sum_distance += math.fabs(m[4] + m[5] + m[6] + m[7] - -2)
	sum_distance += math.fabs(m[8] + m[9] + m[10] + m[11] - -2)
	sum_distance += math.fabs(m[12] + m[13] + m[14] + m[15] - -2)

	sum_distance += math.fabs(m[0] + m[4] + m[8] + m[12] - -2)
	sum_distance += math.fabs(m[1] + m[5] + m[9] + m[13] - -2)
	sum_distance += math.fabs(m[2] + m[6] + m[10] + m[14] - -2)
	sum_distance += math.fabs(m[3] + m[7] + m[11] + m[15] - -2)

	sum_distance += math.fabs(m[0] + m[5] + m[10] + m[15] - -2)
	sum_distance += math.fabs(m[12] + m[9] + m[6] + m[3] - -2)

	return sum_distance

def random_cell():
	return random.randrange(0, 16, 1)

def step():
	if (random.randrange(0, 2, 1)):
		return 1
	return -1


matrix = []
matrix.append(1)
matrix.append(1)
matrix.append(1)
matrix.append(1)

matrix.append(1)
matrix.append(1)
matrix.append(1)
matrix.append(1)

matrix.append(1)
matrix.append(1)
matrix.append(1)
matrix.append(1)

matrix.append(1)
matrix.append(1)
matrix.append(1)
matrix.append(1)


step_matrix = []
while (distance(matrix) != 0):
	step_matrix = list(matrix)
	step_matrix[random_cell()] += step()
	print distance(step_matrix)
	#wait = raw_input("PRESS ENTER TO CONTINUE.")

	if (distance(step_matrix) < distance(matrix)):
		matrix = list(step_matrix)

print matrix

