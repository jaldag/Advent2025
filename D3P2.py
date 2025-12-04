jolt = 0

with open("D3Input.txt") as file:
	while line := file.readline().strip():
		num = ""
		priorIndex = 0
		for x in range(1, 12):
			num += max(line[priorIndex:(-12+x)])
			priorIndex += line[priorIndex:(-12+x)].find(max(line[priorIndex:(-12+x)])) + 1

		num += max(line[priorIndex:])
		jolt += int(num)


print(jolt)