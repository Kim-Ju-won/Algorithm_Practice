import sys

money = int(sys.stdin.readline())

print(int(money * 0.78), int(money * 0.8 + money * 0.2 * 0.78))
