# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret=[]
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1::]:
                ret.append(i)
                ret.append(nums[i+1::].index((target-nums[i]))+i+1)
        return ret