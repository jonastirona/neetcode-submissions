class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += (string + "~")

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        current = ""
        for character in s:
            if character == "~":
                result.append(current)
                current = ""
            else:
                current+=character

        return result
