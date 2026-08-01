class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num = set(nums)

        longest = 0

        for x in num:

            if (x-1) not in num:

                length = 1

                while (x+length) in num:
                    length += 1
                
                longest = max(length,longest)
        return longest

             

        