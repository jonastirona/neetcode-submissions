class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += (str(len(string)) + "#" + string)
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            print("i current character: " + s[i] + " " + str(i))
            current_len = ""
            while s[i].isdigit():
                print("appending current " + s[i] + " to current_len")
                current_len += s[i]
                i+=1
            current_len = int(current_len)
            current_word = ""

            if current_len == 0:
                result.append("")
                i+=1
                continue

            for j in range(i+1, i+1+current_len):
                print("j current character: " + s[j])
                current_word+=s[j]

            i = j+1
            result.append(current_word)

            
        return result


        return result
