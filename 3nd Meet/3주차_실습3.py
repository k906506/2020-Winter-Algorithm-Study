def preorder(root, tree, visit, depth_list, depth): # 전위탐색을 진행하면서 방문 순서와 탐색 깊이를 저장한다
    visit.append(root)
    depth_list.append(depth)
    depth += 1
    if tree[root][0] != '.':
        preorder(tree[root][0], tree, visit, depth_list, depth)
        visit.append(root)
        depth -= 1
        depth_list.append(depth)
    depth += 1
    if tree[root][1] != '.':
        preorder(tree[root][1], tree, visit, depth_list, depth)
        visit.append(root)
        depth -= 1
        depth_list.append(depth)

    return visit, depth_list

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
    depth_list = []
    depth = 0
    visit, depth_list = preorder(root, tree, visit, depth_list, depth)
    
    find = list(input().split())    # 질의 노드
    first_index = visit.index(find[0])  # 방문 순서가 저장된 리스트에서 질의 노드를 처음 방문한 index를 찾는다
    second_index = visit.index(find[1])

    if first_index > second_index:  # 탐색을 위해 오름차순으로 정렬해준다
        first_index, second_index = second_index, first_index

    max_depth = depth_list[first_index]
    for i in range(first_index+1, second_index+1): # 주어진 구간 안에서 최대 깊이를 찾는다
        if depth_list[i] < max_depth:
            max_depth = depth_list[i]
    
    max_index = depth_list.index(max_depth) # 최대 깊이의 index를 저장한다

    print(visit[max_index])

if __name__ == "__main__":
    main()