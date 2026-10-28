class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return [[]]

        result = []
        mp = {}

        for s in strs:
 
            st = "".join(sorted(s))
            
            if st in mp:
                result[mp[st]].append(s)
            else:
                result.append([s])
                mp[st] = len(result) - 1
        
        return result