from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        if len(strs) < 1:
            return lcp
        if len(strs) == 1:
            return strs[0]
        
        for i in range(0, len(strs[0])):
            common_c = strs[0][i]
            flag = True
            for s in strs[1:]:
                flag = i < len(s) and s[i] == common_c
                if not flag:
                    break
            if not flag:
                break    
            else:
                lcp += common_c
        return lcp
    
s = Solution()
ans = s.longestCommonPrefix(["aaa", "a", "bb"])
print(ans)           
                
