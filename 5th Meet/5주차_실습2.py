def main():
    n = int(input())
    input_list = [0 for _ in range(n)]
    count = [0 for _ in range(n)]
    for i in range(n):
        a, b = map(int, input().split())
        input_list[i] = [a, b]
        count[i] = 0    # 먹고 먹히는 것을 표시하기 위한 리스트

    sum_all = n
    input_list = sorted(input_list, key = lambda x : (x[0], x[1]))
    for i in range(n):
        for j in range(i+1, n):
            if input_list[i][0] <= input_list[j][0] and input_list[i][1] <= input_list[j][1] and count[i] >= 0 and count[j] >= 0 and count[j] <= 2:
                sum_all -= 1    # 한 종류의 미생물이 먹혔으므로 -1
                count[i] = -1   # j 미생물에게 먹힌 i 미생물
                count[j] += 1   # j 미생물이 다른 미생물을 먹은 횟수

    print(sum_all)

if __name__ == "__main__":
    main()