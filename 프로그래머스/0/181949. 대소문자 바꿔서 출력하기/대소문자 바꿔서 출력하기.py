str = input()
for c in str : 
    if 'a' <= c <= 'z':
        print(c.upper(),end='')
    elif 'A' <= c <= 'Z':
        print(c.lower(),end='')
        
