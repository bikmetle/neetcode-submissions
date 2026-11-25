class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        sorted_numbers = sorted(counts, key=counts.get, reverse=True)

        return sorted_numbers[:k]
