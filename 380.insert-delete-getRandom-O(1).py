from random import choice
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.d = {}
    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.nums)
        self.nums.append(val)
        return True
    #!!! 这道问题的关键不是插入，而是删除---怎样做到O(1)时间从List内删除元素呢?
    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        id = self.d[val]
        self.nums[id] = self.nums[-1]
        self.d[self.nums[-1]] = id
        self.nums.pop()
        del self.d[val]
        return True
    def getRandom(self) -> int:
        return choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()