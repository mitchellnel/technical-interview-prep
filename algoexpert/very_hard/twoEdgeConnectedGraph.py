# O(v + e) time | O(v) space
def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
        return True

    arrival_times = [-1 for _ in edges]
    start_vtx = 0

    # modified DFS
    if get_min_arrival_time_of_ancestors(start_vtx, -1, 0, arrival_times, edges) == -1:
        return False

    return are_all_vertices_visited(arrival_times)


def are_all_vertices_visited(arrival_times):
    for time in arrival_times:
        if time == -1:
            return False

    return True


def get_min_arrival_time_of_ancestors(
    curr_vtx, parent, curr_time, arrival_times, edges
):
    arrival_times[curr_vtx] = curr_time

    min_arrival_time = curr_time

    for dest in edges[curr_vtx]:
        if arrival_times[dest] == -1:
            # not yet visited
            min_arrival_time = min(
                min_arrival_time,
                get_min_arrival_time_of_ancestors(
                    dest, curr_vtx, curr_time + 1, arrival_times, edges
                ),
            )
        elif dest != parent:
            # we've visited, so there's potentiall lower arrival time
            min_arrival_time = min(min_arrival_time, arrival_times[dest])

    if min_arrival_time == curr_time and parent != -1:
        return -1
    else:
        return min_arrival_time
