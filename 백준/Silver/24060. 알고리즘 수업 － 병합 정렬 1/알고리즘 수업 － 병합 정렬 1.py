import sys
sys.setrecursionlimit(10**6)

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(arr, start, middle, end, count) :
    i = start
    j = middle+1
    temp = []
    while i <= middle and j <= end :
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else :
            temp.append(arr[j]) 
            j += 1
    
    while i <= middle : # 왼쪽 배열 부분이 남은 경우
        temp.append(arr[i]) 
        i += 1
    while j <= end : # 오른쪽 배열 부분이 남은 경우
        temp.append(arr[j]) 
        j += 1
    
    i = start
    t = 0
    while i <= end : # 결과를 A[p..r]에 저장
        arr[i] = temp[t]
        count.append(arr[i])
        i+=1
        t+=1
    return count
    
def merge_sort(arr,start,end, count): # A[p..r]을 오름차순 정렬한다.
    if start < end:
        middle = (start + end) // 2      # q는 p, r의 중간 지점
        merge_sort(arr, start, middle,count)      # 전반부 정렬
        merge_sort(arr, middle+1, end,count)  # 후반부 정렬
        return merge(arr, start, middle, end,count)       # 병합
    else : 
        return count
    


n, k = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
count = []

ans = merge_sort(arr,0,n-1,count)
if len(ans) >= k : 
    print(ans[k-1])
else : 
    print(-1)