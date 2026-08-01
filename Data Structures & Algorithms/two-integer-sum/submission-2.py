class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        k = {} 

        for i,n in enumerate(nums):

            diff = target - n

            if diff in k:
                return [k[diff], i]
        
            k[n] = i
            


            