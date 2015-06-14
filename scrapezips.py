import json
import os

houston = []
houston_extra = [77204, 77225, 77235, 77251, 77269, 77373, 43451]

for i in range(98):
	houston.append(77002+i)

houston.extend(houston_extra)

print(houston)

zip_codes = open(os.getcwd() + '/zip_code_test_file.js', 'r')

zips = json.load(zip_codes)

print(zips['features'][0]['properties']['ZCTA5CE10'])