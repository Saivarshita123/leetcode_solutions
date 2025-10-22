from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort each word to get the anagram key
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        # Return grouped lists
        return list(anagrams.values())
