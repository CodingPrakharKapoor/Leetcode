class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can_cross(day: int) -> bool:
            grid=[[0]*col for _ in range(row)]
            for i in range(day):
                r,c=cells[i]
                grid[r-1][c-1]=1
            q=deque()
            vis=[[0]*col for _ in range(row)]
            for c in range(col):
                if(grid[0][c]==0):
                    q.append((0,c))
                    vis[0][c]=1
            while(q):
                r,c=q.popleft()
                if(r==row-1):
                    return True
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if(0<=nr<row and 0<=nc<col and not vis[nr][nc] and grid[nr][nc]==0):
                        vis[nr][nc]=1
                        q.append((nr,nc))
            return False

        l,r=1,len(cells)
        ans=0
        while(l<=r):
            m=(l+r)//2
            if(can_cross(m)):
                ans=m
                l=m+1
            else:
                r=m-1
        return ans