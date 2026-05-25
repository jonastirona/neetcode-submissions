class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans = ans + word + "~"
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        current = ""
        for char in s:
            if char == '~':
                ans.append(current)
                current = ""
                continue
            current = current + char

        return ans