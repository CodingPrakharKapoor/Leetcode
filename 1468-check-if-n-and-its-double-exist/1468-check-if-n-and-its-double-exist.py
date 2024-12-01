class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if(len(arr)==1):
            return False
        
        seen=set()
        for num in arr:
            if(num*2 in seen or num%2==0 and num//2 in seen):
                return True
            seen.add(num)
        return False