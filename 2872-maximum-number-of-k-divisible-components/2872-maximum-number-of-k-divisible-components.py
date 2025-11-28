class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj=defaultdict(list)
        self.ans=0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node,parent):
            total=values[node]
            for i in adj[node]:
                if(i!=parent):
                    total+=dfs(i,node)
            if(total%k==0):
                self.ans+=1
                return 0
            return total%k
        
        dfs(0,-1)
        return self.ans