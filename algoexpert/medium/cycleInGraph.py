# O(v + e) time | O(v) space
def cycleInGraph(edges):
    for start in range(len(edges)):
        if dfs(edges, start):
            return True

    return False


def dfs(edges, start):
    stack = [start]
    seen = set()

    while len(stack) > 0:
        curr = stack.pop()

        if start in edges[curr]:
            return True

        seen.add(curr)

        for neighbour in edges[curr]:
            if neighbour not in seen:
                stack.append(neighbour)

    return False
