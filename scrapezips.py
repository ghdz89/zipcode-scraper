import json

houston = []
houston_extra = [77204, 77225, 77235, 77251, 77269, 77373, 43451]

for i in range(98):
	houston.append(77002+i)

houston.extend(houston_extra)

print(houston)