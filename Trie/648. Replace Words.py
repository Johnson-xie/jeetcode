from pprint import pprint


class Solution:
    def replaceWords(self, dict, sentence) -> str:

        trie = {}
        for word in dict:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["#"] = True
        pprint(trie)

if __name__ == '__main__':
    dict = ["cat", "bat", "rat", "car", "bbq", "bad", "bqq"]
    sol = Solution()
    sol.replaceWords(dict, 's')