mat = [[1, 9, 13, 36, 51], [24, 12, 16, 20, 1], [14, 33, 1, 23, 26]]
res = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

req = [100, 60, 50, 50, 40]
supply = [50, 100, 150]

cost = 0

i = 0
j = 0

while (i < len(mat) and j < len(mat[0])):

	if(supply[i] == 0):
		i = i + 1
	if(req[j] == 0):
		j = j + 1

	if(supply[i] <= req[j]) :

		res[i][j] = supply[i]
		cost += res[i][j]*mat[i][j]

		if(supply[i] == req[j]):
		
			supply[i] = 0
			req[j] = 0
			i = i + 1
			j = j + 1
		
		else:
			req[j] -= supply[i]
			supply[i] = 0
			i = i + 1
	else:

		res[i][j] = req[j]
		cost += res[i][j]*mat[i][j]

		supply[i] -= req[j]
		req[j] = 0
		j = j + 1

# print(res) 
print("Total cost : " + str(cost))