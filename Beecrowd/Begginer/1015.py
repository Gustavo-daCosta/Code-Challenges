from math import sqrt

p1 = str(input()).split(" ")
p2 = str(input()).split(" ")

distance = sqrt((float(p2[0]) - float(p1[0])) ** 2 + (float(p2[1]) - float(p1[1])) ** 2)

print(f"{distance:.4f}")
