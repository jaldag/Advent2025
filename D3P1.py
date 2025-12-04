jolt = 0

with open("D3Input.txt") as file:
	while line := file.readline().strip():
		jolt += int(max(line[:-1])) * 10 + int(max(line[line.find(max(line[:-1]))+1:]))

print(jolt)