class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for val,count in freq.items():
            buckets[count].append(val)

        ans = []

        for f in range(len(nums),0,-1):
            for val in buckets[f]:
                ans.append(val)

                if len(ans)==k:
                    return ans