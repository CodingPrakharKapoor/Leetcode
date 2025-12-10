class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        freq=defaultdict(int)
        for i in complexity:
            freq[i]+=1
        if(freq[complexity[0]]!=1 or complexity[0]!=min(complexity)):return 0
        return math.factorial(len(complexity)-1)%int(1e9+7)