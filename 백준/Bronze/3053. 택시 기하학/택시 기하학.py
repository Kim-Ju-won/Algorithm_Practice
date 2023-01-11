import sys, math

n = int(sys.stdin.readline())

area = round(n*n*math.pi, 7)
euclid = (n**2)* 2

print("{:.6f}".format(area))
print("{:.6f}".format(euclid))