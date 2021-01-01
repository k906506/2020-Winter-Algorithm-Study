parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(vertices, edges, n):
    for u in vertices:
        make_set(u)

    edges.sort()
    sum = 0

    for e in edges:
        cost, u, v = e      # 가중치, 시작, 도착
        if find(u) != find(v):  # 시작 정점과 도착 정점의 부모가 다를 경우
            union(u,v)
            sum += cost

    return sum

def main():
    n, m = map(int, input().split())
    vertices = []
    edges = []
    vertices = input().split()

    for _ in range(m):
        u, v, c = input().split()
        c = int(c)
        edges.append((c, u, v))     # 가중치, 시작, 도착
    
    standard = kruskal(vertices, edges, n)  # 기준이 되는 MST

    new_edges = []
    result = []     # 중요한 길을 저장할 리스트
    for i in edges:
        new_edges = edges.copy()
        new_edges.remove(i)
        if kruskal(vertices, new_edges, n) > standard:  # MST 값이 커지면 제거한 엣지가 중요한 길
            result.append([i[1], i[2]])
    
    print(len(result))

if __name__ == "__main__":
    main()