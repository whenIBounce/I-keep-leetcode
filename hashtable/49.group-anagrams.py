#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            key = tuple(sorted(word))
            d[key] = d.get(key, []) + [word]
        
        return d.values()
        
# @lc code=end

