class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()

        for n in nums:
            counts[n] = counts.get(n,0)+1

        frequencis = [[] for _ in range(len(nums)+1)]
        for number, frequency in counts.items():
            frequencis[frequency].append(number)

        result = []
        for i in range(len(frequencis)-1, 0, -1):
            for number in frequencis[i]:
                result.append(number)
                if len(result) == k:
                    return result
