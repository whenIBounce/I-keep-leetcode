from typing import List
class Solution:
    #!!!  Method1: Almost there, but the space among words are not evenly
    #!!! distributed
    def fullJustify2(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur = ""
        for i in range(len(words)):
            w = words[i]

            if len(cur) + len(w) == maxWidth or len(cur) + len(w) + 1 == maxWidth:
                ans.append(cur+w)
                cur = ""
            # 1 accounts for at least one space between current line and w
            elif len(cur) + len(w) + 1 < maxWidth:
                cur = cur + w + " "
            elif len(cur) + len(w) > maxWidth:
                cur_words = cur.split()
                words_count = len(cur_words)
                if words_count == 1:
                    extra_space_size = maxWidth - len(cur_words[0])
                    tmp = cur_words[0] + (extra_space_size*" ")
                    ans.append(tmp)
                else:
                    space_size = (maxWidth - len("".join(cur_words)))//words_count
                    tmp = (space_size*" ").join(cur_words[0:-1])
                    last_space_size = maxWidth - len(tmp) - len(cur_words[-1])
                    tmp = tmp + (last_space_size*" ") + cur_words[-1]
                    ans.append(tmp)
                
                cur = w + " "
            if i == len(words)-1:
                extra_space_size = maxWidth - len(cur)
                cur = cur + extra_space_size*" "
                ans.append(cur)

        for line in ans:
            print(line)
                   
        return ans
    
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur_words = []
        cur_length = 0

        for word in words:
            if cur_length + len(cur_words) + len(word) <= maxWidth:
                cur_words.append(word)
                cur_length += len(word)
            else:
                line = self.createLine(cur_words, cur_length, maxWidth)
                ans.append(line)
                cur_words = [word]
                cur_length = len(word)

        last_line = " ".join(cur_words)
        last_line = last_line + " " * (maxWidth - len(last_line))
        ans.append(last_line)

        return ans

    def createLine(self, words: List[str], cur_length: int, maxWidth: int) -> str:
        num_words = len(words)
        num_spaces = maxWidth - cur_length
        if num_words == 1:
            return words[0] + " " * num_spaces

        min_spaces = num_spaces // (num_words - 1)
        extra_spaces = num_spaces % (num_words - 1)

        line = ""
        for i in range(num_words - 1):
            line += words[i]
            line += " " * min_spaces
            if extra_spaces > 0:
                line += " "
                extra_spaces -= 1

        line += words[-1]
        return line

    
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16

# words = ["Science","is",
#          "what","we","understand","well",
#          "enough","to","explain","to",
#          "a","computer.","Art","is",
#          "everything","else","we","do"]
# maxWidth = 20

words = ["This", "is", "an",
         "example", "of", "text", "justification."]
maxWidth = 16




s = Solution()
s.fullJustify(words, maxWidth)
    
            
                    
                    
                