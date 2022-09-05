class Solution(object):
    def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            result=target-nums[i]
            print(nums[i+1:len(nums)])
            if result in nums[i+1:len(nums)]:
                a = nums.reverse()
                return [i,len(nums)-nums.index(result)-1]

s=Solution
s.twoSum([3,2,4],6)