import heapq

def prim(edges, vertices, n):
    queue = []
    heapq.heappush(queue, [0, vertices[0], vertices[1]])    # 가중치, 시작, 도착

    visit = {}
    for i in vertices:
        visit[i] = False

    sum = 0

    while queue:
        h = heapq.heappop(queue)
        if visit[h[2]] == True:     # 도착지점 방문여부 확인
            continue
        else:
            visit[h[2]] = True
            sum += h[0]     # 가중치 합산
        
        for e in edges[h[2]]:   # 다음 도착지점
            if (visit[e[0]]) : continue # 다음 도착지점 방문여부 확인
            heapq.heappush(queue, [e[1], h[2], e[0]])   # 가중치, 시작, 도착
            
    for e in visit.values():    # 방문하지 않은 노드가 있을 경우(고립된 노드 존재)
        if e == False:
            sum = 0
            break

    return sum

def main():
    n, m = map(int, input().split())
    vertices = input().split()
    edges = {}

    for i in vertices:
        edges[i] = []

    for _ in range(m):
        u, v, c = input().split()   #시작, 도착, 가중치
        c = int(c)
        edges[u].append([v, c])     #양방향 그래프
        edges[v].append([u, c])

    print(prim(edges, vertices, n))

if __name__ == "__main__":
    main()