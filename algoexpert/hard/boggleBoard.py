class Trie:
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

    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                break
            node = node[char]
        return self.end_symbol in node


# O(ws + nm*8^s) time | O(ws + nm) space
def boggleBoard(board, words):
    trie = construct_trie_from_words(words)

    contained_words = {}

    visited = [[False for _ in row] for row in board]

    for row in range(len(board)):
        for col in range(len(board[row])):
            traverse_for_words(board, trie.root, row, col, contained_words, visited)

    return [string for string in words if string in contained_words]


def construct_trie_from_words(words):
    trie = Trie()

    for word in words:
        trie.insert(word)

    return trie


def traverse_for_words(board, trie_node, row, col, contained_words, visited):
    if visited[row][col]:
        return

    char = board[row][col]

    if char not in trie_node:
        return

    visited[row][col] = True

    trie_node = trie_node[char]

    if "*" in trie_node:
        contained_words[trie_node["*"]] = True

    neighbours = get_neighbours(board, row, col)
    for neighbour in neighbours:
        nei_row, nei_col = neighbour
        traverse_for_words(board, trie_node, nei_row, nei_col, contained_words, visited)

    visited[row][col] = False


def get_neighbours(board, row, col):
    neighbours = []

    max_rows = len(board)
    max_cols = len(board[row])

    # north
    if row - 1 >= 0:
        neighbours.append((row - 1, col))
    # south
    if row + 1 < max_rows:
        neighbours.append((row + 1, col))
    # west
    if col - 1 >= 0:
        neighbours.append((row, col - 1))
    # east
    if col + 1 < max_cols:
        neighbours.append((row, col + 1))
    # north-west
    if row - 1 >= 0 and col - 1 >= 0:
        neighbours.append((row - 1, col - 1))
    # north-east
    if row - 1 >= 0 and col + 1 < max_cols:
        neighbours.append((row - 1, col + 1))
    # south-west
    if row + 1 < max_rows and col - 1 >= 0:
        neighbours.append((row + 1, col - 1))
    # south-east
    if row + 1 < max_rows and col + 1 < max_cols:
        neighbours.append((row + 1, col + 1))

    return neighbours
