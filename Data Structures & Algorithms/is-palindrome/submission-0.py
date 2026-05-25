class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        news = ""
        reverseds = ""

        for i in range(len(s)):
            if s[i].isalnum():
                news+=s[i]
        
        for j in range(len(news)-1, -1, -1):
            reverseds+=news[j]
            
        print(reverseds)
        print(news)

        return reverseds==news
