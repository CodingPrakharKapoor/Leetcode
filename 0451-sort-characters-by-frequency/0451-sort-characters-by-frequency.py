reversed_dict=lambda d:dict(reversed(d.items()))
sort_by_values=lambda d:dict(sorted(d.items(),key=lambda item:item[1]))
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        freq=reversed_dict(sort_by_values(freq))
        s=""
        for i in freq:
            s+=i*freq[i]
            print(s)
        return s