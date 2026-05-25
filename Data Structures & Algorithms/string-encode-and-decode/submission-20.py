class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''.join(f"{len(s)}#{s}" for s in strs)
        print(result)
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            current_len = int(s[i:j])
            print(f"current_len: {current_len}")

            i = j+1
            print(f"appending {s[i:i+current_len]}")
            result.append(s[i:i+current_len])

            i += current_len
        return result
