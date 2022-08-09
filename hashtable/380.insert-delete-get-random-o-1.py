import random


class RandomizedSet:

# In python, creating a simple api for a set() would be a perfect solution if not for the third operation, getRandom(). 

# We know that we can retrieve an item from a set, and not know what that item will be, but that would not be actually random. 

# (This is due to the way python implements sets. In python3, when using integers, elements are popped from the set in the order they appear in the underlying hashtable. Hence, not actually random.)

# A set is implemented essentially the same as a dict in python, so the time complexity of add / delete is on average O(1). 

# When it comes to the random function, however, we run into the problem of needing to convert the data into a python list in order to return a random element. 

# That conversion will add a significant overhead to getRandom, thus slowing the whole thing down.

# Instead of having to do that type conversion (set to list),
# we can take an approach that involves maintaining both a list and a dictionary side by side. 

    def __init__(self):
        self.data_map = {}
        self.data = []
        

    def insert(self, val: int) -> bool:
        nonExisted = val not in self.data_map
        if nonExisted:
            self.data_map[val] = len(self.data)
            self.data.append(val)
        return nonExisted

    def remove(self, val: int) -> bool:
        existed = val in self.data_map
        if existed:
            # get the index of 'element to remove'
            index_of_val_to_remove = self.data_map[val]
            # get the last element
            last_element_in_list = self.data[-1]
            # switch pos of 'element to remove' and 'last element'
            self.data[index_of_val_to_remove] = last_element_in_list
            self.data[-1] = val
            #update 'last element' index
            self.data_map[last_element_in_list] = index_of_val_to_remove
            # delete val in both list and dict
            self.data.pop()
            self.data_map.pop(val)
        return existed

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
