from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  # YOUR ANSWER
  for i in (0, len(nums)):
    for j in (i+1, len(nums)):
      if nums[i]+nums[j] == target and i != j :
        answer = list((i, j))
        # print(answer)
        return answer

  # print('impossible')
  # return

twoSum([2, 7, 11,15], 9)