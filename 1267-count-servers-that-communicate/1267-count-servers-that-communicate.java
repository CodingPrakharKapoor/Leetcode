class Solution {
    public int countServers(int[][] grid) {
        int not=0;
        int count=0;
        for(int x[]:grid)
        {
            for(int y:x)
            {
                count+=y;
            }
        }
        System.out.println(count);

        for(int x=0;x<grid.length;x++)
        {
            for(int y=0;y<grid[0].length;y++)
            {
                if(grid[x][y]==1 && nothere(grid,x,y,grid.length,grid[0].length))not++;
            }
        }
        return count-not;
    }

    public boolean nothere(int grid[][],int i,int j,int m, int n)
    {
        int count1=0;
        int count2=0;
        for(int x=0;x<m;x++)
        {
            count1+=grid[x][j];
        }
        for(int y=0;y<n;y++)
        {
            count2+=grid[i][y];
        }
        return count1==1 && count2==1;
    }
}