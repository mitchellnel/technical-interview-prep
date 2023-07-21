from collections import deque


class ParenthesesString:
    def __init__(self, string, open_count, close_count):
        self.string = string
        self.open_count = open_count
        self.close_count = close_count

    def __repr__(self):
        return self.string


def generate_valid_parentheses(n):
    result = []

    queue = deque([ParenthesesString("", 0, 0)])
    while len(queue) > 0:
        ps = queue.popleft()

        # if we've reached the maximum number of closed and open parentheses,
        #   then add to our result array
        if ps.open_count == n and ps.close_count == n:
            result.append(ps)
            continue

        # if we can add an open parenthesis, then add it
        if ps.open_count < n:
            queue.append(
                ParenthesesString(ps.string + "(", ps.open_count + 1, ps.close_count)
            )

        # if we can add a close parenthesis, then add it
        if ps.close_count < ps.open_count:
            queue.append(
                ParenthesesString(ps.string + ")", ps.open_count, ps.close_count + 1)
            )

    return result


# recursive solution
def generate_valid_parentheses_recursive(n):
    result = []

    parentheses_string = [0 for _ in range(2 * n)]
    generate_valid_parentheses_recursive_helper(n, 0, 0, parentheses_string, 0, result)

    return result


def generate_valid_parentheses_recursive_helper(
    n, open_count, close_count, parentheses_string, idx, result
):
    # if we've reached the maximum number of open and close parentheses, add it
    #   to the result array
    if open_count == n and close_count == n:
        result.append("".join(parentheses_string))
        return

    # if we can add an open parenthesis, add it
    if open_count < n:
        parentheses_string[idx] = "("
        generate_valid_parentheses_recursive_helper(
            n, open_count + 1, close_count, parentheses_string, idx + 1, result
        )

    # if we can add a close parenthesis, add it
    if close_count < open_count:
        parentheses_string[idx] = ")"
        generate_valid_parentheses_recursive_helper(
            n, open_count, close_count + 1, parentheses_string, idx + 1, result
        )


def main():
    print(
        "All combinations of balanced parentheses are: "
        + str(generate_valid_parentheses(2))
    )
    print(
        "All combinations of balanced parentheses are: "
        + str(generate_valid_parentheses(3))
    )


main()
