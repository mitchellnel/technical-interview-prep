class Solution:
    def simplifyPath(self, path):
        stack = []

        for directory in path.split("/"):
            if directory == "..":
                if len(stack) > 0:
                    stack.pop()
            elif len(directory) > 0 and directory != ".":
                stack.append(directory)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()

    assert sol.simplifyPath("/home/") == "/home"
    assert sol.simplifyPath("/../") == "/"
    assert sol.simplifyPath("/home//foo/") == "/home/foo"
    assert sol.simplifyPath("/a/./b/../../c/") == "/c"
    assert sol.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"

    print("All test cases passed.")
