rows = []
with open("D7Input.txt") as file:
	while line := file.readline().strip():
		rows.append(line)

beams = {rows[0].index('S')}

splitCount = 0

for i in range(1, len(rows)):
	split = set()
	remove = set()
	for j in beams:
		if rows[i][j] == '^':
			splitCount+=1
			remove.add(j)
			split.add(j-1)
			split.add(j+1)
	beams.update(split)
	beams = beams - remove

print(splitCount)
