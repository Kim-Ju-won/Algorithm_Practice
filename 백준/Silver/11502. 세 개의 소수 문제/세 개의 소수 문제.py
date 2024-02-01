import sys


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


t = int(sys.stdin.readline())
queries = [int(sys.stdin.readline()) for _ in range(t)]
prime_set = set()
for i in range(2, max(queries) + 1):
    if is_prime(i):
        prime_set.add(i)
prime_list = list(prime_set)
prime_list.sort()
for query in queries:
    find_ans = False
    for i in range(len(prime_list)):
        for j in range(i, len(prime_list)):
            for k in range(j, len(prime_list)):
                if prime_list[i] + prime_list[j] + prime_list[k] == query:
                    print(prime_list[i], prime_list[j], prime_list[k])
                    find_ans = True
                    break
            if find_ans == True:
                break
        if find_ans == True:
            break
    if find_ans == False:
        print(0)
