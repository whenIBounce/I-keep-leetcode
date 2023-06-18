from collections import defaultdict
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words)
        w = len(words[0])
        
        wmap = defaultdict(int)
        for word in words:
            wmap[word] += 1
        ans = []
        for i in range(0, n-(m*w)+1):
            tmp = defaultdict(int)
            j = 0
            while j < m*w:
                cur = s[i+j:i+j+w]
                tmp[cur] += 1
                if tmp[cur] > wmap[cur]:
                    break
                j += w
            if j == w*m:
               ans.append(i)
        
        return ans            
            
s = Solution()
s.findSubstring("saasdsda", ["aa", "bb", "ss"])