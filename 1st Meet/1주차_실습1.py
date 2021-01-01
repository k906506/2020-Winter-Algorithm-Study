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

    print(len(node_dict[find_node]))

if __name__ == "__main__":
    main()