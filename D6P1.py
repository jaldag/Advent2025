rows = []
with open("D6Input.txt") as file:
	while line := file.readline().strip():
		rows.append(line.split(" "))

strippedRows = []

for row in rows:
	strippedRows.append([int(s) if s.isdigit() else s for s in row if s.strip()])

total = 0

for i in range(0, len(strippedRows[0])):
	operation = strippedRows[-1].pop(0)
	num = strippedRows[0][i]
	for j in range(1, len(strippedRows) - 1):
		if operation == "+":
			num += strippedRows[j][i]
		else:
			num *= strippedRows[j][i]
	total += num

print(total)