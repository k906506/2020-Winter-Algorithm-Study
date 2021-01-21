def find_path(subject_dict, count, first):
    visited = []
    while first:
        first.sort(reverse=True)
        e = first.pop()
        visited.append(e)
        for i in range(len(subject_dict[e])):
            count[subject_dict[e][i]] -= 1
            if count[subject_dict[e][i]] == 0:
                first.append(subject_dict[e][i])
    return visited

def main():
    n, m = map(int, input().split())
    subject_dict = {}
    count = {}
    first = []

    subject = list(input().split())
    for i in range(n):
        subject_dict[subject[i]] = []
        count[subject[i]] = 0

    for _ in range(m):
        i, j = input().split()
        subject_dict[i].append(j)
        count[j] += 1  
    
    for i in subject:
        if count[i] == 0:
            first.append(i)
    
    result = find_path(subject_dict, count, first)
    print(*result)

if __name__ == "__main__":
    main()