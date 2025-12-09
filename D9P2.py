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

for area in areas:
	row1 = rows[area[1]]
	row2 = rows[area[2]]
	lowX = row1[0] if row1[0] < row2[0] else row2[0]
	highX = row1[0] if row1[0] > row2[0] else row2[0]
	lowY = row1[1] if row1[1] < row2[1] else row2[1]
	highY = row1[1] if row1[1] > row2[1] else row2[1]

	good = True
	for i in range(0, len(rows)):
		#at end of the list, last point connects to first point
		if i == len(rows) - 1:
			point1 = rows[i]
			point2 = rows[0]
		else:
			point1 = rows[i]
			point2 = rows[i+1]

		#Check if any edges are inside the box. If so, it's not good
		if not ((point1[1] >= highY and point2[1] >= highY) or (point1[1] <= lowY and point2[1] <= lowY) or (point1[0] >= highX and point2[0] >= highX) or (point1[0] <= lowX and point2[0] <= lowX)):
			good = False
			break
	if good:
		print(area[0])
		break