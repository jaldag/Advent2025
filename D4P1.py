grid = []
accessCount = 0

with open("D4Input.txt") as file:
	while line := file.readline().strip():
		grid.append(line)

for x in range(0, len(grid)):
	for y in range(0, len(grid[x])):
		paperCount = 0
		if grid[x][y] == ".":
			continue
		if x > 0 and grid[x-1][y] == "@":
			paperCount += 1
		if x < len(grid) - 1 and grid[x+1][y] == "@":
			paperCount += 1
		if y > 0 and grid[x][y-1] == "@":
			paperCount += 1
		if y < len(grid[x]) - 1 and grid[x][y+1] == "@":
			paperCount += 1

		if x > 0 and y > 0 and grid[x-1][y-1] == "@":
			paperCount += 1
		if x > 0 and y < len(grid[x]) - 1 and grid[x-1][y+1] == "@":
			paperCount += 1
		if x < len(grid) - 1 and y > 0 and grid[x+1][y-1] == "@":
			paperCount += 1
		if x < len(grid) - 1 and y < len(grid[x]) - 1 and grid[x+1][y+1] == "@":
			paperCount += 1

		if paperCount < 4:
			accessCount+= 1

print(accessCount)