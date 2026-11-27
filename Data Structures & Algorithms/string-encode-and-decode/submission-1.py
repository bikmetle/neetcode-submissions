class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for item in strs:
            length = len(item)
            result.append(f"{length}#{item}")

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1

            item_length = int(s[left:right])
            item = s[right+1:right+1+item_length]
            result.append(item)
            left = right+item_length+1

        return result
