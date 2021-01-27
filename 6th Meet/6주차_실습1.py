def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == "__main__":
    main()