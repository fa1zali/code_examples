# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure 
# to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

# Author: Faisal Ali
# Creation Date: 06-Feb-2021
# Version 1.0

class ecommerce:
    def __init__(self):
        self.stack_list = []
    
    def record(self, order_id):
        self.order_id = order_id
        self.stack_list.append(self.order_id)
    
    def get_last(self, i):
        self.i = i
        print(self.stack_list[(self.i -1)])

    def log(self):
        print(self.stack_list)

obj = ecommerce()
obj.record(122)
obj.record(324)
obj.record(500)
obj.log()
obj.get_last(2)