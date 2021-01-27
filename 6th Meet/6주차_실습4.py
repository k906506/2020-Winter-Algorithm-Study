def main():
    n, m = map(int, input().split())    # 행, 열
    map_list = [[0] for _ in range(n)]

    for i in range(n):
        map_list[i] = list(map(int, input().strip().split()))
    
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        dp[n-1][i] = map_list[n-1][i] # 맨 아래열 초기화

    for i in range(n-2, -1, -1): # 아래에서 위로
        for j in range(m):
            if j == 0: # 맨 좌측열
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + map_list[i][j]
            elif j == m-1: # 맨 우측열
                dp[i][j] = max(dp[i+1][j], dp[i+1][j-1]) + map_list[i][j]
            else: # 나머지
                dp[i][j] = max(dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1]) + map_list[i][j]

    print(max(dp[0]))

if __name__ == "__main__":
    main()