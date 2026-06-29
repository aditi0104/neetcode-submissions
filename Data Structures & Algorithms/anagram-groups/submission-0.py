from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for word in strs:
            anagramDict["".join(sorted(word))].append(word)
        return list(anagramDict.values())