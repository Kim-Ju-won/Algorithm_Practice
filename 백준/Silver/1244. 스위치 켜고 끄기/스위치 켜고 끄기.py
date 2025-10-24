import sys

n = int(sys.stdin.readline())
arr = [0]+list(map(int, sys.stdin.readline().split()))
people = int(sys.stdin.readline())
cards = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(people) ]

for card in cards : 
    gender, number = card 
    if gender == 1 : # 남자
        for i in range(number, n+1, number): 
            arr[i] = 1 - arr[i]
    elif gender == 2 : # 여자 
        k = 0
        while number - k > 0 and number + k <= n :
            if k == 0 : 
                arr[number] = 1 - arr[number]
            else : 
                if arr[number-k] == arr[number+k] : 
                    arr[number-k] = 1 - arr[number-k]
                    arr[number+k] = 1 - arr[number+k]
                else : 
                    break
            k += 1

for idx, ele in enumerate(arr[1:]) :

    if idx != 0 and idx%20 == 0 : 
        print("\n"+f"{ele}", end= " ")
    else : 
        print(ele, end=" ")
