class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        lst=[]
        for a,b in rectangles:
            lst.append(min(a,b))
        m=max(lst)
        return lst.count(m)