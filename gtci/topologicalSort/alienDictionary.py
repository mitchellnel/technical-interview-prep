def find_order(words):
    if len(words) == 0:
        return ""

    topological_order = []

    # a. Initialise the graph
    indegrees = {}
    graph = {}

    for word in words:
        for character in word:
            # put a value in both the maps for every unique character -- keys are unique
            indegrees[character] = 0
            graph[character] = []

    # b. Build the graph
    for i in range(0, len(words) - 1):
        w1, w2 = words[i], words[i + 1]

        for j in range(0, min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]

            # if the two characters are different
            if parent != child:
                # create a directed edge from parent to child
                # put the child into its parent's list
                if child not in graph[parent]:
                    graph[parent].append(child)

                    # increment indegree
                    indegrees[child] += 1

                # only the first difference helps us
                break

    # c. Find the sources
    queue = []
    for node in indegrees:
        if indegrees[node] == 0:
            queue.append(node)

    # d. Topoologically sort
    while len(queue) > 0:
        curr_node = queue.pop(0)

        topological_order.append(curr_node)
        for child in graph[curr_node]:
            indegrees[child] -= 1

            if indegrees[child] == 0:
                queue.append(child)

    if len(topological_order) != len(graph):
        return ""

    return "".join(topological_order)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
