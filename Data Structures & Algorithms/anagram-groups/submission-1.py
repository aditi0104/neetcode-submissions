from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for word in strs:
            lst = [0]*26
            for char in word:
                lst[ord(char) - ord('a')] += 1
            lst = tuple(lst)
            anagramDict[lst].append(word)
        return list(anagramDict.values())