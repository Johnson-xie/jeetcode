class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = []

        for index, word in enumerate(words):

            for word2 in words[:index] + words[index + 1:]:
                if word in word2:
                    ret.append(word)
                    break

        return ret

    def stringMatching2(self, words: List[str]) -> List[str]:
        arr = " ".join(words)
        return [word for word in words if arr.count(word) >= 2]

    def stringMatching3(self, words: List[str]) -> List[str]:
        """字典树解法

        按长度逆序排列，短单词只可能是比他更长单词的字串，反之一定不成立

        """
        def add(word: str):
            node = trie
            for c in word:
                node = node.setdefault(c, {})

        def get(word: str) -> bool:
            node = trie
            for c in word:
                if (node := node.get(c)) is None: return False
            return True

        words.sort(key=len, reverse=True)
        trie, result = {}, []
        for word in words:
            if get(word): result.append(word)
            for i in range(len(word)):
                add(word[i:])
        return result

