fresh = set()

with open("D5Input.txt") as file:
	ranges, ids = [item.splitlines() for item in file.read().strip().split("\n\n")]

numRanges = []

for line in ranges:
	numRanges.append([int(line.split("-")[0]), int(line.split("-")[1])])

numRanges.sort()

compress = [numRanges.pop(0)]

for start, end in numRanges:
	if start > compress[-1][1]:
		compress.append([start, end])
	else:
		compress[-1][1] = max(end, compress[-1][1])

total = 0

for start, end in compress:
	total += end - start + 1

print(total)