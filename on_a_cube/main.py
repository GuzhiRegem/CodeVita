#!/usr/bin/python3
"""
    on_a_cube
    module
    return: nothing
"""
import sys

if len(sys.argv) < 2:
	print("usage: ./main.py <filename>")
	exit()

points = []
with open(sys.argv[1], "r") as f:
	tmp = f.read().split('\n')[1].split(',')
	print(tmp)
	while (len(tmp) > 0):
		lis = [int(tmp[0]), int(tmp[1]), int(tmp[2])]
		points.append(lis)
		tmp.pop(0)
		tmp.pop(0)
		tmp.pop(0)
for a in points:
	if 0 in a:
		continue
	if 10 in a:
		continue
	print("{} is invalid point".format(a))
	exit()

print(points)
