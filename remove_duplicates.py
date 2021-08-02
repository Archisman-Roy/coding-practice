# Problem statement
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

def removeDuplicates(nums:List[int]) -> int:
  
  # counter
  duplicate_counter = 0
  
  # duplicate cache
  duplicate_cache = {}
  
  # length of input array
  l = len(nums)
  
  # walk through the list
  for i in range(l):
    # add to the counter if current element == last element
    if(i != 0 and nums[i]==nums[i-1]):
      duplicate_counter = duplicate_counter + 1
      duplicate_cache[nums[i]] = 1
    else:
      duplicate_cache[nums[i]] = 0
  
  # push duplicate to the end
  for i in range(l):
    if duplicate_cache[nums[i]] == 1:
      nums.pop(i)

  # return length
  return l - duplicate_counter

# test cases
print("---------------------------------------")
print("---------------------------------------")
inp_list = [0,0,0,0,3]
print(f"Input list: {inp_list}")
k = removeDuplicates(inp_list)
print(f"Number of unique elements: {k}")
print(f"Output list: {inp_list}")
print("---------------------------------------")
print("---------------------------------------")
inp_list = [0,0,1,1,1,2,2,3,3,4]
print(f"Input list: {inp_list}")
k = removeDuplicates(inp_list)
print(f"Number of unique elements: {k}")
print(f"Output list: {inp_list}")
print("---------------------------------------")
print("---------------------------------------")