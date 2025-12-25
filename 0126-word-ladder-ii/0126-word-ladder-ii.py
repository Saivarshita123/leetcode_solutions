from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Step 1: BFS
        parents = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        found = False
        word_len = len(beginWord)

        while queue and not found:
            level_visited = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(word_len):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            if new_word not in distance:
                                distance[new_word] = distance[word] + 1
                                parents[new_word].append(word)
                                level_visited.add(new_word)
                                if new_word == endWord:
                                    found = True
                            elif distance[new_word] == distance[word] + 1:
                                parents[new_word].append(word)
            queue.extend(level_visited)
            wordSet -= level_visited

        # Step 2: DFS backtracking
        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [p])

        if found:
            dfs(endWord, [endWord])

        return res
