pos = 50
count = 0

with open("D1Input.txt") as file:
	while line := file.readline():
		if line[0] == "R":
			pos = (pos + int(line[1:])) % 100
		else:
			pos = (pos - int(line[1:])) % 100
		if pos == 0:
			count += 1


print(count)