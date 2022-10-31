# O(n) time | O(1) space
def runLengthEncoding(string):
    encoded = ""

    current_run_char = None
    current_run_len = 0

    if len(string) == 1:
        return "1" + string

    for idx, char in enumerate(string):
        if current_run_char is None:
            current_run_char = char
            current_run_len = 1
            continue

        if char == current_run_char:
            current_run_len += 1

            if current_run_len == 10:
                encoded += "9" + current_run_char
                current_run_len = 1
        else:
            encoded += str(current_run_len) + current_run_char

            current_run_char = char
            current_run_len = 1

        if idx == len(string) - 1:
            encoded += str(current_run_len) + current_run_char

    return encoded
