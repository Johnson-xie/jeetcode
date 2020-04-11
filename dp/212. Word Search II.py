from pprint import pprint


class Solution:

    def __init__(self):
        self.root = {}
        self.output = set()

    def findWords(self, board, words):

        if not board or not board[0] or not words:
            return []

        self.build_trie(words)

        # direct
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.rows = len(board)
        self.cols = len(board[0])

        for x in range(self.rows):
            for y in range(self.cols):
                if board[x][y] in self.root:
                    self.dfs(board, x, y, "", self.root)
        return self.output

    def build_trie(self, words):

        for word in words:
            node = self.root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["#"] = True

    def dfs(self, board, x, y, word, node):

        word += board[x][y]
        print(word)
        node = node[board[x][y]]

        if "#" in node:
            self.output.add(word)

        visted, board[x][y] = board[x][y], 0
        for dx, dy in zip(self.dx, self.dy):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and board[nx][ny] != 0 and board[nx][ny] in node:
                self.dfs(board, nx, ny, word, node)
        board[x][y] = visted


if __name__ == '__main__':
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    sol = Solution()
    ret = sol.findWords(board, words)
    print(ret)