class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums.sort()
        val = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != val:
                val = nums[i]
            else:
                return True
        return False