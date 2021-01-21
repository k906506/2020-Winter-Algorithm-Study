import math

def heuristics(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def oil_path(edge_dict, n, m, src_x, src_y, dst_x, dst_y):
    open_list = []
    close_list = []

    for i in edge_dict[(src_x,src_y)]:
        G = i[1]
        H = heuristics(i[0][0], i[0][1], dst_x, dst_y)
        F = G + H
        open_list.append([i[0], F, G, H])

    open_list = sorted(open_list, key = lambda x : -x[1])
    close_list.append(open_list.pop())

    while True:
        check_open_list = []
        check_close_list = []
        for i in open_list:
            check_open_list.append(i[0])
        for i in close_list:
            check_close_list.append(i[0])
        
        if (dst_x, dst_y) in check_close_list:
            break

        for i in range(len(close_list)):
            for j in edge_dict[close_list[i][0]]:
                if j[0] in check_close_list:
                    continue
                G = j[1] + close_list[i][2]
                if ((dst_x-1 <= j[0][0] <= dst_x+1) and (dst_y == j[0][1])) or ((dst_x == j[0][0]) and (dst_y-1 <= j[0][1] <= dst_y+1)):
                    H = 0
                else:
                    H = heuristics(j[0][0], j[0][1], dst_x, dst_y)
                F = G + H
                if j[0] in check_open_list:
                    if [j[0], F, G, H][1] < open_list[check_open_list.index(j[0])][1]:
                        open_list[check_open_list.index(j[0])] = [j[0], F, G, H]
                else:
                    open_list.append([j[0], F, G, H])

        open_list = sorted(open_list, key = lambda x : -x[1])
        close_list.append(open_list.pop())
    
    return close_list[len(close_list)-1][2]

def main():
    n, m, oil = map(int, input().split())
    map_list = [[] for _ in range(n)]
    edge_dict = {}

    src_x = 0
    src_y = 0
    dst_x = 0
    dst_y = 0

    for i in range(n):
        map_list[i] = list(input())
    
    # src와 dst가 (0, 0), (n-1, n-1)이 아닌 경우도 있으므로 좌표를 찾는다.
    for i in range(n):
        for j in range(m):
            if map_list[i][j] == "S":
                src_x = j
                src_y = i
                map_list[i][j] = 0
            elif map_list[i][j] == "E":
                dst_x = j
                dst_y = i
                map_list[i][j] = 0
    
    for i in range(n):  #행
        for j in range(m):  #열
            edge = []
            if i != 0:
                edge.append([(j, i-1), int(map_list[i-1][j])])
            if i != n-1:
                edge.append([(j, i+1), int(map_list[i+1][j])])
            if j != 0:
                edge.append([(j-1, i), int(map_list[i][j-1])])
            if j != m-1:
                edge.append([(j+1, i), int(map_list[i][j+1])])
            edge_dict[j, i] = edge

    answer = oil_path(edge_dict, n, m, src_x, src_y, dst_x, dst_y)

    if oil >= answer:
        print(oil-answer)
    else:
        print("Not enough oil!")

if __name__ == "__main__":
    main()