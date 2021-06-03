# Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

# record(timestamp): records a hit that happened at timestamp
# total(): returns the total number of hits recorded
# range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

# Author: Faisal Ali
# Creation Date: 03-June-2021
# Version 1.0
# Not using timestamp, more of simplified version of same, will make it more complex in later builds

class HitCounter():

    def __init__(self):
        """Creates an empty list for storing the timestamps"""
        self.record_list = list()

    def record(self, timestamp):
        """Adds the timestamps in the list and also sorts the same"""
        self.timestamp = timestamp
        self.record_list.append(self.timestamp)
        self.record_list.sort()
    
    def total(self):
        """Returns the count of timestamps"""
        return len(self.record_list)
    
    def range(self, lower, upper):
        """Takes the upper and lower range and returns the total hits including the limits as well"""
        self.lower = lower
        self.upper = upper
        if self.lower in self.record_list and self.upper in self.record_list: 
            self.lower_index = self.record_list.index(self.lower)
            self.upper_index = self.record_list.index(self.upper)
            self.range_list = self.record_list[self.lower_index : self.upper_index+1]
            return len(self.range_list)
        return "Index not available"


obj = HitCounter()
obj.record(1)
obj.record(9)
obj.record(3)
obj.record(4)
obj.record(6)
obj.record(2)
obj.record(5)
print(obj.total())
print(obj.range(0,9))