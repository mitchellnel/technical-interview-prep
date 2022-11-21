class SmallStringTrie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def insert(self, string):
        node = self.root
        for char in string:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_symbol] = string


# O(ns + bs) time | O(ns) space
def multiStringSearch(bigString, smallStrings):
    trie = SmallStringTrie()

    for string in smallStrings:
        trie.insert(string)

    contained_strings = {}
    for i in range(len(bigString)):
        find_small_strings_in_trie(trie, bigString, i, contained_strings)

    return [string in contained_strings for string in smallStrings]


def find_small_strings_in_trie(trie, string, start_idx, contained_strings):
    node = trie.root
    for i in range(start_idx, len(string)):
        char = string[i]
        if char not in node:
            break

        node = node[char]

        if trie.end_symbol in node:
            contained_strings[node[trie.end_symbol]] = True
