import math

rows = []
with open("D6Input.txt") as file:
	while line := file.readline().replace("\n", ""):
		rows.append(line)

total = 0
nums = []

#Each line is the same length
#Iterate through the line's length backwards
for i in range(len(rows[0])-1, -1, -1):
	num = ""
	#Build the number from the column, ignoring last operational row
	for j in range(0, len(rows) - 1):
		if rows[j][i].isdigit():
			num += rows[j][i]
	#Skip column if empty column
	if num == "":
		continue
	nums.append(int(num))

	#If last row at position 'i' is an operation, it's time to math the numbers together
	#After, reset the numbers to be math'd
	if rows[-1][i] != ' ':
		operation = rows[-1][i]
		if operation == "+":
			total += sum(nums)
		else:
			total += math.prod(nums)
		nums = []

print(total)