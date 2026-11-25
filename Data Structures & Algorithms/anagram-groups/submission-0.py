class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for word in strs:
            word_counter = str(sorted(word))
            if word_counter in anagrams:
                anagrams[word_counter].append(word)
            else:
                anagrams[word_counter] = [word]
        
        return [value for key, value in anagrams.items()]
