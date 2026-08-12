class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        # Build frequency map for s1
        for char in s1:
            s1_count[char] = 1 + s1_count.get(char, 0)

        left = 0

        for right in range(len(s2)):
            # Add current character to window
            window_count[s2[right]] = 1 + window_count.get(s2[right], 0)

            # If window became too large, remove left character
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1

                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                left += 1

            # Only compare when window size == len(s1)
            if right - left + 1 == len(s1):
                if window_count == s1_count:
                    return True

        return False