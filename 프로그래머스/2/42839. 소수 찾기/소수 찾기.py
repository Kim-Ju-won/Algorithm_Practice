from itertools import permutations


def is_prime(n):
    if n >= 2:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return 0
        return 1
    else:
        return 0


def solution(numbers):
    answer = 0
    n = len(numbers)
    all_options = set()
    for k in range(n, 0, -1):
        options = list(permutations(numbers, k))
        for opt in options:
            all_options.add(int("".join(opt)))
    for option in all_options:
        answer += is_prime(option)
    return answer
