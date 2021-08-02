# Problem statement
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

def removeDuplicates(arr: List[int]) -> int:

  n = len(arr)

  if n == 0 or n == 1:
    return n

  # To store index of next unique element
  j = 0

  # maintaining the index of next unique element 
  # make a swap of the unique element when found 
  for i in range(0, n-1):
    if arr[i] != arr[i+1]:
      arr[j] = arr[i]
      j += 1

  arr[j] = arr[n-1]
  j += 1
  return j

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