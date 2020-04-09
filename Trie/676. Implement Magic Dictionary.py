import collections


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def buildDict(self, dict) -> None:
        """
        Build a dictionary through a list of words
        """

        # for word in dict:
        #     node = self.root
        #     for char in word:
        #         node = node.setdefault(char, {})
        #     node["end"] = True
        self.words = set(dict)
        ret = [word[:i] + "*" + word[i + 1:] for word in dict for i in range(0, len(word))]
        self.counters = collections.Counter(
            [word[:i] + "*" + word[i + 1:] for word in dict for i in range(0, len(word))])
        print(self.counters)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i in range(len(word)):
            neigh = word[:i] + "*" + word[i + 1:]
            if self.counters[neigh] > 1 or (self.counters[neigh] == 1 and word not in self.words):
                return True
        return False


class MagicDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = collections.defaultdict(list)

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """

        # for word in dict:
        #     node = self.root
        #     for char in word:
        #         node = node.setdefault(char, {})
        #     node["end"] = True

        for word in dict:
            self.root[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """

        for pat in self.root[len(word)]:
            flag = False
            for i, j in zip(pat, word):
                if i != j:
                    if not flag:
                        flag = True
                    else:
                        break
            else:
                if flag:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
if __name__ == '__main__':
    mag = MagicDictionary()
    words = ["hello","leetcode"]
    mag.buildDict(words)
    print(mag.search("hello"))