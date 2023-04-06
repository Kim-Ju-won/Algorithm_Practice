import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
words_frequency = dict()

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if len(s) >= m : 
        if s in words_frequency:
            words_frequency[s] += 1
        else : 
            words_frequency[s] = 1

frequency_order_dict = dict()

for word, frequency in words_frequency.items():
    if frequency in frequency_order_dict : 
        frequency_order_dict[frequency].append(word)
    else : 
        frequency_order_dict[frequency] = [word]

for word in frequency_order_dict : 
    frequency_order_dict[word].sort(key=lambda x : (-len(x),x))

keys = list(frequency_order_dict.keys())
keys.sort(reverse=True)

for key in keys : 
    for ele in frequency_order_dict[key] :
        print(ele) 