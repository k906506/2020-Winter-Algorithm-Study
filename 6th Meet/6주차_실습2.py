def knapsack(W, weight_list, value_list, n):
    item_cnt = len(value_list)
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(1, item_cnt):
        for j in range(W+1):
            value = value_list[i]
            weight = weight_list[i]
            if weight > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])
    return dp[item_cnt-1][W]

def main():
    W = int(input())
    n = int(input())
    input_weight = [0] + list(map(int, input().split()))
    input_value_list = [0] + list(map(int, input().split()))
    print(knapsack(W, input_weight, input_value_list, n))

if  __name__ == "__main__":
    main()