import heapq

def dijkstra(v_dic, v_list, V, E, src, dst):
    INF = float('inf')
    distance = {}
    for i in range(V):
        distance[v_list[i]] = INF
    distance[src] = 0
    queue = []
    prev = {}
    for i in range(V):
        prev[v_list[i]] = []
    found = {}
    for i in range(V):
        found[v_list[i]] = False
    
    heapq.heappush(queue, [0, src])
    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True
        for node_weight in v_dic[v[1]]:
            if (found[node_weight[0]]):
                continue
            if (distance[node_weight[0]] > distance[v[1]] + node_weight[1]):
                distance[node_weight[0]] = distance[v[1]] + node_weight[1]
                heapq.heappush(queue, [distance[node_weight[0]], node_weight[0]])
                prev[node_weight[0]] = [v[1], node_weight[0], node_weight[1]]
    return distance[dst]

def main():
    V, E = map(int, input().split())
    v_list = input().split()
    v_dic = {}
    for i in v_list:
        v_dic[i] = []

    for _ in range(E):
        i, j, c = input().split()
        c = int(c)
        v_dic[i].append([j,c])
        v_dic[j].append([i,c])
    
    len_dic = {}
    for i in v_list:
        len_dic[i] = []

    min_len = int(input())

    for i in v_list:
        for j in v_list:
            result = dijkstra(v_dic, v_list, V, E, i, j)
            if min_len >= result:
                len_dic[i].append(result)
                len_dic[j].append(result)
    
    result = []
    
    for i in range(len(len_dic)):
        result.append([v_list[i],len_dic[v_list[i]]])
    result = sorted(result, key = lambda x : len(x[1]))
    print(result[len(result)-1][0], int(len(result[len(result)-1][1])//2))

if __name__ == "__main__":
    main()