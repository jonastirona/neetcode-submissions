class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num]+=1

        buckets = [[] for i in range (len(nums) + 1)]

        for key, value in frequencies.items():
            buckets[value].append(key)

        final = []
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                final.append(num)
                if len(final) == k:
                    return final

        return final