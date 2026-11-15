class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        right=len(numbers)-1
        list1=[]
        while left!=right:
            sum1=numbers[left]+numbers[right]
            if sum1==target:
                list1.append(left+1)
                list1.append(right+1)
                return list1
            elif sum1>target:
                right-=1
            else:
                left+=1        

        