pos = 50
count = 0

with open("D1Input.txt") as file:
	while line := file.readline():
		oldPos = pos
		if line[0] == "R":
			pos = (pos + int(line[1:]))
		else:
			if pos == 0:
				count -= 1 # Don't count if starting on 0 and going negative
			pos = (pos - int(line[1:]))

		if pos <= 0 or pos >= 100:
			if pos <= 0:
				pos -= 100
			count += abs(int(pos / 100))
			pos = pos % 100

print(count)