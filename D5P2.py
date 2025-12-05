fresh = 0

with open("D5Input.txt") as file:
	ranges, ids = [item.splitlines() for item in file.read().strip().split("\n\n")]

for num in ids:
	for line in ranges:
		if int(num) >= int(line.split("-")[0]) and int(num) <= int(line.split("-")[1]):
			fresh += 1
			break
print(fresh)