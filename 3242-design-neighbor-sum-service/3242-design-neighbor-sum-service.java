class NeighborSum {
    static class Node
    {
        int x;
        int y;
        Node(int x,int y)
        {
            this.x=x;
            this.y=y;
        }
    }

    int ar[][];
    int n;
    Map<Integer,Node>map=new HashMap<>();

    public NeighborSum(int[][] grid) {
        this.ar=grid;
        this.n=grid.length;
        for(int x=0;x<n;x++)
        {
            for(int y=0;y<n;y++)
            {
                Node node=new Node(x,y);
                map.put(grid[x][y],node);
            }
        }
    }
    
    public int adjacentSum(int value) {
        Node node=map.get(value);
        int x=node.x;
        int y=node.y;
        int ans=0;
        if(x!=0)ans+=ar[x-1][y];
        if(y!=0)ans+=ar[x][y-1];
        if(x!=n-1)ans+=ar[x+1][y];
        if(y!=n-1)ans+=ar[x][y+1];
        return ans;
    }
    
    public int diagonalSum(int value) {
        Node node=map.get(value);
        int x=node.x;
        int y=node.y;
        int ans=0;
        if(0<=x-1 && x-1<n && 0<=y-1 && y-1<n)
            ans+=ar[x-1][y-1];
        if(0<=x+1 && x+1<n && 0<=y-1 && y-1<n)
            ans+=ar[x+1][y-1];
        if(0<=x-1 && x-1<n && 0<=y+1 && y+1<n)
            ans+=ar[x-1][y+1];
        if(0<=x+1 && x+1<n && 0<=y+1 && y+1<n)
            ans+=ar[x+1][y+1];
        return ans;
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = new NeighborSum(grid);
 * int param_1 = obj.adjacentSum(value);
 * int param_2 = obj.diagonalSum(value);
 */