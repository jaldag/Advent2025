import re
import itertools

rows = []

with open("D10Input.txt") as file:
	while line := file.readline().strip():
		rows.append([re.search(r"\[(.*)\]", line).group(1), re.search(r"\](.*)\{", line).group(1).strip().split(" "), [int(x) for x in re.search(r"\{(.*)\}", line).group(1).split(",")]])

buttonPushes = 0
for row in rows:
	desiredPattern = row[0]
	for x in range(1, 10):
		found = False
		nums = list(map(lambda a: re.sub(r'[^0-9]', '', a), row[1]))
		for it in list(itertools.combinations_with_replacement(nums, x)):
			joinedNums = [b for sub in it for b in sub]
			if found:
				break
			match = True
			for y in range(len(desiredPattern)):
				if not (joinedNums.count(str(y)) % 2 == 0 and desiredPattern[y] == "." or joinedNums.count(str(y)) % 2 == 1 and desiredPattern[y] == "#"):
					match = False
					break
				
			if match:
				buttonPushes += x
				found = True
				break
		if found:
			break

print(buttonPushes)