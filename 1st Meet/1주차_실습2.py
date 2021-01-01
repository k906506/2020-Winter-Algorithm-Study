def bfs(node_dict, node):
    visit = []
    queue = []
    queue.append(node)
    while queue:
        element = queue.pop(0)
        if element not in visit:
            visit.append(element)
            queue.extend(node_dict[element])
    return visit

def main():
    n, m = map(int, input().split())
    node = list(input().split())
    node_dict = dict()

    for i in range(n):
        node_dict[node[i]] = []
    
    for i in range(m):
        srt, dst = input().split()
        if dst not in node_dict[srt]:
            node_dict[srt].append(dst)
    
    find_node = input()
    print(*bfs(node_dict, find_node))

if __name__ == "__main__":
    main()