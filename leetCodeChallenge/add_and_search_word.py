"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.insert(word)

    def search(self, word):
        return self.trie.dotSearch(word)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i, ch in enumerate(word):
            if (ch not in node.children):
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isLast = True

    def search(self, word):
        node = self.root
        for ch in word:
            if (ch not in node.children):
                return False
            node = node.children[ch]
        return node.isLast

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if (ch not in node.children):
                return False
            node = node.children[ch]
        return True

    #search for words with ".", which matches any char
    def dotSearch(self, word):
        def dfs(node, word):
            if not word:
                return node.isLast
            ch = word[0]
            if ch == '.':
                for n in [node.children[_] for _ in node.children]:
                    if dfs(n, word[1:]):
                        return True
            else:
                if ch in node.children:
                    if dfs(node.children[ch], word[1:]):
                        return True
                    else:
                        return False
        return dfs(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
