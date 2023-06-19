from collections import defaultdict
from typing import List
class Solution:
    # Method 1: Sorting
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for str in strs:
            tmp = ''.join(sorted(str))
            if tmp not in m:
                m[tmp] = [str]
            else:
                m[tmp].append(str)
        ans = []
        for key in m:
            ans.append(m[key])
        return ans
    # Method 2: Countint
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for str in strs:
            count = [0]*26
            for ch in str:
                count[ord(ch)-ord('a')] += 1
            mp[tuple(count)].append(str)
        return list(mp.values())
        
s = Solution()
print(s.groupAnagrams([""]))