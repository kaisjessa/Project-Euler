cubes = []
cube_lists = []

for n in range(10**4):
	cubes.append(n**3)

	temp = sorted(list(str(n**3)))
	cube_lists.append(temp)
	if cube_lists.count(temp) >= 5:
		for cube in cubes:
			if sorted(list(str(cube))) == temp:
				print(cube)
				quit()
