class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num]+=1

        sorted_counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_counts[i][0])

        return result
