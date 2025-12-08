import math

rows = []
distances = list()
circuits = []

with open("D8Input.txt") as file:
	while line := file.readline().strip():
		rows.append([int(x) for x in line.split(',')])

#math.dist() will find the euclidean distance between two points
#For each combination of rows, calculate the distance and save as [distance, row1 index, row2 index]
#Then, sort the distances in ascending order of distance
for i in range(0, len(rows) - 1):
	for j in range(i+1, len(rows)):
		distances.append([math.dist(rows[i], rows[j]) ,i, j])
distances.sort()

#Check against all distances, but will break early if a full circuit is made
for i in range(0, len(distances)):
	existingCircuit = False
	#If an existing circuit contains one of the row indexes already, add the row indexes to the circuit set
	for circuit in circuits:
		if distances[i][1] in circuit or distances[i][2] in circuit:
			circuit.add(distances[i][1])
			circuit.add(distances[i][2])
			existingCircuit = True
	#If the row indexes are not in an existing circuit, create a new circuit set
	if not existingCircuit:
		circuits.append({distances[i][1], distances[i][2]})

	#Run through all the circuits, and combine sets if there is any intersection between them
	for j in range(0, len(circuits) - 1):
		for k in range(j+1, len(circuits)):
			if len(circuits[j].intersection(circuits[k])) > 0:
				circuits[j] = circuits[j].union(circuits[k])
				circuits[k] = set()
	#Remove the empty sets that had values merged into other sets
	circuits = [circuit for circuit in circuits if circuit]

	#If there is only one circuit in the set, and that circuit contains all row values, we're done.
	if len(circuits) == 1 and len(circuits[0]) == 1000:
		print(rows[distances[i][1]][0] * rows[distances[i][2]][0])
		break;