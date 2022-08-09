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
            key = tuple(sorted(word)) # why use tuple as dict[key]? Diff between list and tuple?
            # Diff between sorted() and sort()
            d[key] = d.get(key, []) + [word] # to append the word, [word] is compact, can you use list(word)?
        
        return d.values()
        
# @lc code=end

