class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int m=grid.length;
        int n=grid[0].length;
        if(grid[0][0]==1 || grid[m-1][n-1]==1) return 0;
        int dp[][]=new int[m][n];
        dp[0][0]=1;
        for(int x=0;x<m;x++)
        {
            for(int y=0;y<n;y++)
            {
                if(x==0 && y==0) continue;
                if(grid[x][y]==1) dp[x][y]=0;
                else if(x==0) dp[x][y]=dp[x][y-1];
                else if(y==0) dp[x][y]=dp[x-1][y];
                else dp[x][y]=dp[x-1][y]+dp[x][y-1];
            }
        }
        return dp[m-1][n-1];
    }
}