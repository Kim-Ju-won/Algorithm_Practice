import sys

ans = 0
count = 0 
for _ in range(20):
    subject, credit, grade = sys.stdin.readline().split()
    if grade != 'P':
        count+=float(credit)
        if grade == 'A+': 
            ans += 4.5 * float(credit)
        elif grade == 'A0':
            ans += 4.0 * float(credit)
        elif grade == 'B+':
            ans += 3.5 * float(credit)
        elif grade == 'B0':
            ans += 3.0 * float(credit)
        elif grade == 'C+':
            ans += 2.5 * float(credit)
        elif grade == 'C0':
            ans += 2.0 * float(credit)
        elif grade == 'D+':
            ans += 1.5 * float(credit)
        elif grade == 'D0':
            ans += 1.0 * float(credit)
print(f'{round(ans/count,6):.6f}')