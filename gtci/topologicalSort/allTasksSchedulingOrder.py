from copy import deepcopy


def get_all_scheduling_orders(tasks, prerequisites):
    if tasks <= 0:
        return False

    topological_orderings = []

    # a. Initialise the graph
    indegrees = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    # b. Build the graph
    for prereq in prerequisites:
        parent, child = prereq[0], prereq[1]

        graph[parent].append(child)
        indegrees[child] += 1

    # c. Find the sources
    queue = []
    for node in indegrees:
        if indegrees[node] == 0:
            queue.append(node)

    get_all_topological_orderings(graph, indegrees, queue, [], topological_orderings)

    return topological_orderings


def get_all_topological_orderings(
    graph, indegrees, queue, current_topo_order, topological_orderings
):
    if len(queue) > 0:
        for source in queue:
            current_topo_order.append(source)

            # make a copy of the queue for the recursive call
            queue_for_next_call = deepcopy(queue)

            # only remove the current source we're looking at
            #   -- all other sources should remain in the queue for the next call
            queue_for_next_call.remove(source)

            # decrement children indegrees
            for child in graph[source]:
                indegrees[child] -= 1

                # if they've become a source, add them to the queue
                if indegrees[child] == 0:
                    queue_for_next_call.append(child)

            get_all_topological_orderings(
                graph,
                indegrees,
                queue_for_next_call,
                current_topo_order,
                topological_orderings,
            )

            # backtrack -- this source needs to be included in the next source's ordering
            # remove the vertex from the topological ordering, and put all of its children back to
            #   consider the next source instead of the current vertex
            current_topo_order.remove(source)
            for child in graph[source]:
                indegrees[child] += 1

    # if the current_topo_order does not contain all takss, either we've a cyclic dependency
    #   between tasks, or we have not processed all the tasks in this recursive call
    if len(current_topo_order) == len(graph):
        topological_orderings.append(deepcopy(current_topo_order))


def main():
    print("Task Orders: ")
    print(get_all_scheduling_orders(3, [[0, 1], [1, 2]]))

    print("Task Orders: ")
    print(get_all_scheduling_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))

    print("Task Orders: ")
    print(
        get_all_scheduling_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
    )


main()
