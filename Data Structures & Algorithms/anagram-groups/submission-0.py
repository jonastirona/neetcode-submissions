class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0
        anagrams = {}
        groups = []

        for word in strs:
            key = ''.join(sorted(word))
            if key in anagrams:
                groups[anagrams[key]].append(word)
            else:
                anagrams[key] = index
                groups.append([word])
                index+=1
        return groups
