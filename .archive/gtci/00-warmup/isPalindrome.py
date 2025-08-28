def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    s = s.lower()

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


def main():
    # Test case 1: "A man, a plan, a canal, Panama!"
    # Expected output: True
    print(isPalindrome("A man, a plan, a canal, Panama!"))

    # Test case 2: "race a car"
    # Expected output: False
    print(isPalindrome("race a car"))

    # Test case 3: "Was it a car or a cat I saw?"
    # Expected output: True
    print(isPalindrome("Was it a car or a cat I saw?"))

    # Test case 4: "Madam, in Eden, I'm Adam."
    # Expected output: True
    print(isPalindrome("Madam, in Eden, I'm Adam."))

    # Test case 5: "empty string"
    # Expected output: True
    print(isPalindrome(""))


main()
