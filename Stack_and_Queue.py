# File: Stack_and_Queue.py

# Description: Choose a fixed number of elements to maximize final result

# Student Name:

# Student EID:

# Course Name: CS 313E

# Unique Number

import sys

    #add an item to the top of the stack
def push(item, self):
    return self.append(item)

    #remove an item from the top of the stack
def pop(removed_list, self):
    return removed_list.append(self.pop())

    #remove an item from the bottom of the stack
def dequeue(removed_list, self):
    return removed_list.append(self.pop(0))

    #check the item on the top of the stack (but don't remove)
def peek(self):
    return self[-1]

def sum_dict(nums,tgt,pop_num,remove_dict = {}):
    removed_list2 = []

    if pop_num >= 0:
        for i in range(pop_num): #"popping"
            removed_list2.append(nums[-(i+1)])
 
        for j in range(tgt-pop_num): #dequing
            removed_list2.append(nums[j])

        #adding removed list to sum dictionary
        remove_dict[pop_num] = removed_list2
        return sum_dict(nums,tgt,pop_num-1,remove_dict)
    else:
        return remove_dict

# Input: nums is a list of positive integers; tgt is a positive integer indicating how many numbers there should be.
# Output: returns the maximum sum possible of the numbers picked by the rules explained in specifications.
def pop_or_dequeue(nums, tgt):
    remove_dict = sum_dict(nums,tgt,tgt)
    max_sum = 0
    for i in range(tgt+1):
        if sum(remove_dict[i]) > max_sum:
            max_sum = sum(remove_dict[i])
    return max_sum


    
    """STUDENT TODO"""









# TAKE CAUTION TO EDIT BELOW THIS LINE
if __name__ == "__main__":
    input1 = sys.stdin.readline().split()
    num_list = []
    for ele in input1:
        num_list.append(int(ele))
    num = int(sys.stdin.readline())
    print(pop_or_dequeue(num_list, num))
