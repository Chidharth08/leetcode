class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}

        l = 0 

        res = 0

        maxfreq = 0

        
        for r in range(len(s)): 
            
            count[s[r]] = 1 + count.get(s[r],0)
            maxfreq = max(maxfreq, count[s[r]])


            if (r-l+1) - maxfreq > k:
                count[s[l]] -= 1

                if count[s[l]] == 0:
                    del count[s[l]]

                l += 1

            res = max(res, r-l+1)
        return res 

        