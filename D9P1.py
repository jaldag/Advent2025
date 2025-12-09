rows = []
areas = list()

with open("D9Input.txt") as file:
	while line := file.readline().strip():
		rows.append([int(x) for x in line.split(',')])

#Calculate the area between each combination of points, sort by largest area
for i in range(0, len(rows) - 1):
	for j in range(i+1, len(rows)):
		areas.append([(abs(rows[i][0] - rows[j][0]) + 1) * (abs(rows[i][1] - rows[j][1]) + 1) , i, j])
areas.sort(reverse=True)

print(areas[0][0])