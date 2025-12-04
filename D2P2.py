count = 0
total = 0

def isInvalid(num):
	s = str(num)

	for i in range(1, int(len(s)/2)+1):
		if s.count(s[0:i]) * i == len(s):
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