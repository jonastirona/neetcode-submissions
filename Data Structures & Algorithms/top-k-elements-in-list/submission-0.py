class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1

            if num not in frequencies:
                frequencies[num] = 1
        
        sorted_frequencies = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

        final = []
        for i in range(k):
            final.append(sorted_frequencies[i][0])

        return final