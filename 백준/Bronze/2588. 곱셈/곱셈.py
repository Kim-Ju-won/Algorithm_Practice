import sys

num_1 = int(sys.stdin.readline())
num_2 = int(sys.stdin.readline())

print(num_1 * (num_2%10))
print(num_1 * (num_2//10%10))
print(num_1 * (num_2//100%10)) 
print(num_1 * num_2)