import sys

happy_unhappy = sys.stdin.readline().rstrip()

happy = happy_unhappy.count(":-)")
unhappy = happy_unhappy.count(":-(")


if happy + unhappy == 0:
    print("none")
else:
    print("happy" if happy > unhappy else "sad" if unhappy > happy else "unsure")
