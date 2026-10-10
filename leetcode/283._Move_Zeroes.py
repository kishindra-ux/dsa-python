class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 and isinstance(nums[0], list):
            target = nums[0]
        else:
            target = nums

        if len(nums) >= 1 and len(nums) <= 10**4:
            count=0
            for i in range(len(nums)):
                if nums[i] >= -2*31 and nums[i] <= 2*31-1:
                    if nums[i] != 0:
                        nums[count],nums[i]=nums[i],nums[count]
                        count+=1
        
nums = [0,1,0,3,12]
Solution.moveZeroes(0, nums)
print(nums)
