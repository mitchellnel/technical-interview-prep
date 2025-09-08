class Solution:
    def findProvinces(self, isConnected):
        visited = [False] * len(isConnected)
        num_provinces = 0

        for i in range(len(isConnected)):
            if not visited[i]:
                num_provinces += 1
                self.dfs(i, visited, isConnected)

        return num_provinces

    def dfs(self, node, visited, isConnected):
        stack = [node]

        while stack:
            curr = stack.pop()

            visited[curr] = True

            for i in range(len(isConnected[curr])):
                if isConnected[curr][i] == 1 and not visited[i]:
                    stack.append(i)


if __name__ == "__main__":
    sol = Solution()

    assert sol.findProvinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert sol.findProvinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert (
        sol.findProvinces([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]) == 2
    )

    print("All test cases passed.")
