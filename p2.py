#Thanks to https://github.com/BrechtVandevoort/AdventOfCode_2016/blob/master/day_01/day01_2.py

instructions = open('input.txt').read().strip().split(', ')
position = [0,0]
visited = [[0,0]]
direction = 0
for i in instructions:
	rotation = -1 if i[0] == 'L' else 1
	direction = (direction + rotation) % 4
	distance = int(i[1:])
	step = -1 if direction > 1 else 1
	for j in range(distance):
		position[direction % 2] += step
		if position in visited:
			print ('this is the answer', sum(map(abs, position)))
		else:
			visited.append(position[:])