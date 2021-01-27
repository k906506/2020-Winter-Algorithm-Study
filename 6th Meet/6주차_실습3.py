def main():
    n = int(input())
    cut = list(map(int, input().split()))
    wood = int(input())
    INF = float('inf')
    dp = [INF for _ in range(wood+1)]
    
    dp[0] = 0

    cut.sort()  # 오름차순으로 정렬

    for i in range(n):
        for j in range(cut[i], wood+1):
            dp[j] = min(dp[j], dp[j-cut[i]] + 1)
    print(dp[wood])       

if __name__ == "__main__":
    main()