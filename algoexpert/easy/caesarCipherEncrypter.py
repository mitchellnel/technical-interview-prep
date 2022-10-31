# O(n) time | O(1) space
def caesarCipherEncrypter(string, key):
    encrypted = ""
    key = key % 26

    for char in string:
        ascii = ord(char) + key
        encrypted_char = chr(ascii) if ascii <= 122 else chr(96 + ascii % 122)
        encrypted += encrypted_char

    return encrypted
