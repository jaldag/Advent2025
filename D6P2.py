import math

rows = []
with open("D6Input.txt") as file:
	while line := file.readline().replace("\n", ""):
		rows.append(line)

total = 0
nums = []

#Each line is the same length
#Iterate through the line's length
for i in range(0, len(rows[0])):
	#Save the operation if it's in this column
	if rows[-1][i] != ' ':
		operation = rows[-1][i]
	
	#Build the number from the column, ignoring last operational row
	num = ""
	for j in range(0, len(rows) - 1):
		if rows[j][i].isdigit():
			num += rows[j][i]
	#If the column built a number, save it
	if num.isdigit():
		nums.append(int(num))
		#Move on to next column, unless it's the last column
		if i != len(rows[0])-1:
			continue
	#If we're here, it means we're in the last column or in an empty column
	#Time for some quick math
	if operation == "+":
		total += sum(nums)
	else:
		total += math.prod(nums)
	nums = []

print(total)