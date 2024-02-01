import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = [{"left": None, "right": None} for _ in range(26)]
visited = [False] * 26
alphabet_dict = dict()
number_dict = dict()
preorder = []
inorder = []
postorder = []

for i in range(65, 91):
    alphabet_dict[chr(i)] = i - 65
    number_dict[i - 65] = chr(i)
alphabet_dict["."] = None


for _ in range(n):
    root, left, right = sys.stdin.readline().split()
    root, left, right = alphabet_dict[root], alphabet_dict[left], alphabet_dict[right]
    if left != None:
        graph[root]["left"] = left
    if right != None:
        graph[root]["right"] = right


def DFS(k):
    visited[k] = True
    preorder.append(k)
    if graph[k]["left"] != None and visited[graph[k]["left"]] == False:
        DFS(graph[k]["left"])
    inorder.append(k)
    if graph[k]["right"] != None and visited[graph[k]["right"]] == False:
        DFS(graph[k]["right"])
    postorder.append(k)


DFS(0)
for array in [preorder, inorder, postorder]:
    for ele in array:
        print(number_dict[ele], end="")
    print()
