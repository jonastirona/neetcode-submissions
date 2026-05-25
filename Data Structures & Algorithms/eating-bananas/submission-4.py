class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        highest = right

        while left <= right:
            mid = left + (right - left) // 2

            current_time = 0

            for pile in piles:
                if pile <= mid:
                    current_time+=1
                else:
                    current_time+=((pile+mid-1)//mid)

            if current_time <= h:
                right = mid - 1
                highest = min(highest,mid)
            else:
                left = mid + 1

        return highest

"""
piles = [1,4,3,2]
h = 9

h is amount of time you have to eat all bananas
we return a value k, which is banana ber hour eating rate.
however, koko can't move between piles in the same hour

ex: if k = 4, and current pile is 5, it would take 2 hours

brute force solution:
start with k = 1
iterate through piles and calculate time it takes to eat, and if its past h, increment k + 1

inefficient because you would have k = 1, k = 2, k = 3, etc

binary search:
min k = 1, max k = biggest pile
for each k, start in the middle, calculate time taken. compare this to h
"""