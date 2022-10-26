# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    seq_ptr = 0

    if len(array) < len(sequence):
        return False

    for num in array:
        if num == sequence[seq_ptr]:
            seq_ptr += 1

        if seq_ptr == len(sequence):
            return True

    return False
