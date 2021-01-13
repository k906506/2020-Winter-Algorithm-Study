import heapq

def bellman_ford(v_dic, v_list, V, E, src, dst):
    INF = float('inf')
    distance = {}
    for i in v_list:
        distance[i] = INF
    distance[src] = 0
    predecessor = {}
    for i in v_list:
        predecessor[i] = None

    for i in range(V-1):
        for i in v_dic:
            for j, c in v_dic[i]:
                if distance[j] > distance[i] + c:
                    distance[j] = distance[i] + c
                    predecessor[j] = [i, j, c]
    
    for i in v_dic:
        for j, c in v_dic[i]:
            if distance[j] > distance[i] + c:
                return -1
    
    return predecessor

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

    src, dst = input().split()
    predecessor = bellman_ford(v_dic, v_list, V, E, src, dst)

    if predecessor == -1:
        print("Negative Cycle!")
    else:
        prev_list = []
        prev_e = dst

        while prev_e != src:
            prev_list.append(predecessor[prev_e])
            prev_e = predecessor[prev_e][0]

        prev_list.reverse()
    
        for i in prev_list:
         print(*i)

if __name__ == "__main__":
    main()