import random

class RandomizedSet:

    def __init__(self):
        self.nums = []      # Store elements in a list
        self.index_map = {} # Map each value to its index in list

    def insert(self, val: int) -> bool:
        # Value is already in the set, so return False
        if val in self.index_map:
            return False
        
        # Otherwise, add the value to the list and record its index
        self.index_map[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        # Value is not in the set, so return False
        if val not in self.index_map:
            return False
        
        # Get the index of the element to remove
        idx = self.index_map[val]

        # Move last element to the spot of the element to remove
        last_element = self.nums[-1]
        self.nums[idx] = last_element
        self.index_map[last_element] = idx

        # Remove the last element
        self.nums.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        # Return random element from the list
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()