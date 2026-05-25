class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += (string + "~")
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        current = 0
        for i, char in enumerate(s):
            if char == '~':
                decoded.append(s[current:i])
                current = i+1
        
        return decoded