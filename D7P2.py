from collections import defaultdict

rows = []
with open("D7Input.txt") as file:
	while line := file.readline().strip():
		rows.append(line)

beams = {rows[0].index('S')}

timelineDict = defaultdict(int)

timelineDict[rows[0].index('S')] = 1

for i in range(1, len(rows)):
	split = set()
	remove = set()
	for j in beams:
		if rows[i][j] == '^':
			remove.add(j)
			split.add(j-1)
			split.add(j+1)
			#"Kill" the current column, but add this column's timeline count to each sibling
			timelineDict[j-1] += timelineDict[j]
			timelineDict[j+1] += timelineDict[j]
			timelineDict[j] = 0

	beams.update(split)
	beams = beams - remove

print(sum(timelineDict[key] for key in timelineDict))