def main():
    n = int(input())
    parent = []
    child = []
    
    for _ in range(n):
        node = list(input().split())
        if node[1] != '.' or node[2] != '.':
            parent.append(node[0])
            child.append(node[1])
            child.append(node[2])
    
    for i in parent:    # 부모 노드가 저장된 리스트의 원소가
        if i not in child:  # 자식 노드가 저장된 리스트에 없으면
            root = i
            break
    
    print(root)

if __name__ == "__main__":
    main()