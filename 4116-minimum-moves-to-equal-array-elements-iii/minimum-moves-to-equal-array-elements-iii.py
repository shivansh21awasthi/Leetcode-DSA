class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves=0
        mx=max(nums)
        for i in range(len(nums)):
            while nums[i]!=mx:
                nums[i]+=1
                moves+=1
        return moves        


        