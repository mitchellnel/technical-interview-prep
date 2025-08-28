class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_symbol] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_symbol in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


def main():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app")
    assert trie.search("app") == True


main()
