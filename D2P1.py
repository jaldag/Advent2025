count = 0
total = 0

def isInvalid(num):
	if len(str(num)) % 2 == 1:
		return False
	s = str(num)
	half = int(len(s)/2)
	if str(num)[0:half] == str(num)[half:]:
		return True
	return False

line = open("D2Input.txt").readline()

for val in line.split(","):
	start = val[0:val.index("-")]
	end = val[val.index("-")+1:]
	num = int(start)
	while num <= int(end):
		if (isInvalid(num)):
			count += 1
			total += num
		num += 1

print(count)
print(total)