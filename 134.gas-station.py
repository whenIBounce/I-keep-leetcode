from typing import List

class Solution:
    #? This methond is easy to write but hard to understand
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, tank = 0, 0
        for i in range(len(gas)):
            if gas[i] + tank < cost[i]:
                start = i + 1
                tank = 0
            else:
                tank += gas[i] - cost[i]
        return start
    #TODO: WRITE ANOTHER brute force method

s = Solution()

# Test Case 1:
gas1 = [1,2,3,4,5]
cost1 = [3,4,5,1,2]
print(s.canCompleteCircuit(gas1, cost1))  # Expected output: 3

# Test Case 2:
gas2 = [2,3,4]
cost2 = [3,4,3]
print(s.canCompleteCircuit(gas2, cost2))  # Expected output: -1

# Test Case 3:
gas3 = [5,1,2,3,4]
cost3 = [4,4,1,5,1]
print(s.canCompleteCircuit(gas3, cost3))  # Expected output: 4
