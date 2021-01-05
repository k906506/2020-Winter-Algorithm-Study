def preorder(node, tree, visit):
    visit.append(node)
    if tree[node][0] != '.':
        preorder(tree[node][0], tree, visit)
    if tree[node][1] != '.':
        preorder(tree[node][1], tree, visit)
    
    return visit

def inorder(node, tree, visit):
    if tree[node][0] != '.':
        inorder(tree[node][0], tree, visit)
    visit.append(node)
    if tree[node][1] != '.':
        inorder(tree[node][1], tree, visit)

    return visit

def postorder(node, tree, visit):
    if tree[node][0] != '.':
        postorder(tree[node][0], tree, visit)
    if tree[node][1] != '.':
        postorder(tree[node][1], tree, visit)
    visit.append(node)

    return visit

def main():
    n = int(input())
    tree = {}
    parent = []
    child = []
    
    for _ in range(n):
        node = list(input().split())
        tree[node[0]] = [node[1], node[2]]  # tree를 구현한다
        if node[1] != '.' or node[2] != '.':
            parent.append(node[0])
            child.append(node[1])
            child.append(node[2])
    
    for i in parent:    # 부모 노드가 저장된 리스트의 원소가
        if i not in child:  # 자식 노드가 저장된 리스트에 없으면
            root = i
            break
    
    visit = []
    print(*preorder(root, tree, visit))

    visit = []
    print(*inorder(root, tree, visit))

    visit = []
    print(*postorder(root, tree, visit))

if __name__ == "__main__":
    main()