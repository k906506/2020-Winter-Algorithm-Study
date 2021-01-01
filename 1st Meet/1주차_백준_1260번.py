def dfs(node, v, visit = None):
    if visit == None:
        visit = []
    visit.append(v)
    for element in node[v]:
        if element not in visit:
            dfs(node, element, visit)
    return visit

def bfs(node, v):
    visit = []
    queue = []
    queue.append(v)
    while queue:
        element = queue.pop(0)
        if element not in visit:
            visit.append(element)
            queue.extend(node[element])
    return visit

def main():
    n, m, v = map(int, input().split())
    node = dict()

    for i in range(n):
        node[i+1] = []
    
    for i in range(m):
        srt, dst = map(int, input().split())
        if dst not in node[srt]:
            node[srt].append(dst)
        if srt not in node[dst]:
            node[dst].append(srt)

    for i in range(n):
        node[i+1].sort()
    
    print(*dfs(node, v))
    print(*bfs(node, v))

if __name__ == "__main__":
    main()