class LCS:
    def findLCS(self, A, n, B, m):
        dp = [([0]*(m+1)) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if (A[i-1]==B[j-1]):
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # write code here
        return dp[n][m]
