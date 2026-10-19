class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        nums.sort()
        lst=[]
        if target not in nums:
            return []
        for i in range(n):
            if nums[i]==target:
                lst.append(i)
                i+=1
        return lst        