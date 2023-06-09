class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票算法
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
                count += 1
            else:
                if candidate == n:
                    count += 1
                else:
                    count -= 1
        return candidate