def dfs(node_dict, node, visit = None):
    if visit is None:
        visit = []
    visit.append(node)
    for element in node_dict[node]:
        if element not in visit:
            dfs(node_dict, element, visit)
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
    print(*dfs(node_dict, find_node))

if __name__ == "__main__":
    main()