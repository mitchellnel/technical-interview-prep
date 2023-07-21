def different_ways_to_evaluate_expression(expression):
    PLUS_DEF = "+"
    MINUS_DEF = "-"
    MULTIPLY_DEF = "*"

    results = []

    # base case -- if the input string is a number, parse it an add it to the
    #   output
    if (
        PLUS_DEF not in expression
        and MINUS_DEF not in expression
        and MULTIPLY_DEF not in expression
    ):
        results.append(int(expression))
        return results

    for idx, char in enumerate(expression):
        if not char.isdigit():
            # break the expression into two halves, and make recursive calls
            left_part = different_ways_to_evaluate_expression(expression[0:idx])
            right_part = different_ways_to_evaluate_expression(expression[idx + 1 :])

            # evaluate with the operator
            for part1 in left_part:
                for part2 in right_part:
                    if char == PLUS_DEF:
                        results.append(part1 + part2)
                    elif char == MINUS_DEF:
                        results.append(part1 - part2)
                    elif char == MULTIPLY_DEF:
                        results.append(part1 * part2)

    return results


def different_ways_to_evaluated_expression_dp(expression):
    return different_ways_to_evaluated_expression_dp_helper({}, expression)


def different_ways_to_evaluated_expression_dp_helper(dp, expression):
    if expression in dp:
        return dp[expression]

    PLUS_DEF = "+"
    MINUS_DEF = "-"
    MULTIPLY_DEF = "*"

    results = []

    # base case -- if the input string is a number, parse it an add it to the
    #   output
    if (
        PLUS_DEF not in expression
        and MINUS_DEF not in expression
        and MULTIPLY_DEF not in expression
    ):
        results.append(int(expression))
        return results

    for idx, char in enumerate(expression):
        if not char.isdigit():
            # break the expression into two halves, and make recursive calls
            left_part = different_ways_to_evaluated_expression_dp_helper(
                dp, expression[0:idx]
            )
            right_part = different_ways_to_evaluated_expression_dp_helper(
                dp, expression[idx + 1 :]
            )

            # evaluate with the operator
            for part1 in left_part:
                for part2 in right_part:
                    if char == PLUS_DEF:
                        results.append(part1 + part2)
                    elif char == MINUS_DEF:
                        results.append(part1 - part2)
                    elif char == MULTIPLY_DEF:
                        results.append(part1 * part2)

    # memoise
    dp[expression] = results

    return results


def main():
    print(
        "Expression evaluations: "
        + str(different_ways_to_evaluated_expression_dp("1+2*3"))
    )

    print(
        "Expression evaluations: "
        + str(different_ways_to_evaluated_expression_dp("2*3-4-5"))
    )


main()
