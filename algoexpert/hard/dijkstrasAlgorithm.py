# O(v^2 + e) time | O(v) space
def dijkstrasAlgorithm_array(start, edges):
    num_vertices = len(edges)

    min_distances = [float("inf") for _ in range(num_vertices)]
    min_distances[start] = 0

    visited = set()

    while len(visited) < num_vertices:
        vertex, curr_min_dist = get_vertex_with_min_distance(min_distances, visited)

        if curr_min_dist == float("inf"):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            dest, dist = edge

            if dest in visited:
                continue

            new_dist = curr_min_dist + dist
            if new_dist < min_distances[dest]:
                min_distances[dest] = new_dist

    return list(map(lambda x: -1 if x == float("inf") else x, min_distances))


def get_vertex_with_min_distance(distances, visited):
    curr_min_dist = float("inf")
    vertex = None

    for vertex_idx, dist in enumerate(distances):
        if vertex_idx in visited:
            continue
        if dist <= curr_min_dist:
            vertex = vertex_idx
            curr_min_dist = dist

    return vertex, curr_min_dist


class MinHeap:
    def __init__(self, array):
        # holds the position in the heap that each vertex is at
        self.vertex_map = {idx: idx for idx in range(len(array))}
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    # O(n) time | O(1) space
    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for curr_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(curr_idx, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def sift_down(self, curr_idx, end_idx, heap):
        child_one_idx = curr_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = curr_idx * 2 + 2 if curr_idx * 2 + 2 <= end_idx else -1

            if child_two_idx != -1 and heap[child_two_idx][1] < heap[child_one_idx][1]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx

            if heap[idx_to_swap][1] < heap[curr_idx][1]:
                self.swap(curr_idx, idx_to_swap, heap)
                curr_idx = idx_to_swap
                child_one_idx = curr_idx * 2 + 1
            else:
                return

    # O(log(n)) time | O(1) space
    def sift_up(self, curr_idx, heap):
        parent_idx = (curr_idx - 1) // 2
        while curr_idx > 0 and heap[curr_idx][1] < heap[parent_idx][1]:
            self.swap(curr_idx, parent_idx, heap)
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) // 2

    # O(log(n)) time | O(1) space
    def remove(self):
        if self.is_empty():
            return

        self.swap(0, len(self.heap) - 1, self.heap)

        vertex, dist = self.heap.pop()
        self.vertex_map.pop(vertex)
        self.sift_down(0, len(self.heap) - 1, self.heap)

        return vertex, dist

    def swap(self, i, j, heap):
        self.vertex_map[heap[i][0]] = j
        self.vertex_map[heap[j][0]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def update(self, vertex, value):
        self.heap[self.vertex_map[vertex]] = (vertex, value)
        self.sift_up(self.vertex_map[vertex], self.heap)


# O((v+e)log(n)) time | O(v) space
def dijkstrasAlgorithm(start, edges):
    num_vertices = len(edges)

    min_distances = [float("inf") for _ in range(num_vertices)]
    min_distances[start] = 0

    min_dists_heap = MinHeap([(idx, float("inf")) for idx in range(num_vertices)])
    min_dists_heap.update(start, 0)

    while not min_dists_heap.is_empty():
        vertex, curr_min_dist = min_dists_heap.remove()

        if curr_min_dist == float("inf"):
            break

        for edge in edges[vertex]:
            dest, dist = edge

            new_dist = curr_min_dist + dist
            if new_dist < min_distances[dest]:
                min_distances[dest] = new_dist
                min_dists_heap.update(dest, new_dist)

    return list(map(lambda x: -1 if x == float("inf") else x, min_distances))
