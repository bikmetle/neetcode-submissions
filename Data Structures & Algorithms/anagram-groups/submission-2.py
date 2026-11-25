class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            letters = [0]*26
            for w in word:
                index = ord(w) - ord("a")
                letters[index] += 1

            key = tuple(letters)
            anagrams[key].append(word)

        return list(anagrams.values())
