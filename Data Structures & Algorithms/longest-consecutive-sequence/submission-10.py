class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)

        longest= 0

        for x in numset:

            if (x-1) not in numset:

                length = 1
            
                while (x + length) in numset:

                    length += 1
            
                longest = max(length, longest)

        return longest


             

        