class main:
    def __init__(self, key: dict) -> None:
        self.key = key

    def decrypt_caesar(self, ciphertext):
        for shift in range(26):
            decrypted_message = ''
            for char in ciphertext:
                if char.isalpha():
                    decrypted_char = chr(
                        ((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26) + ord('a' if char.islower() else 'A'))
                    decrypted_message += decrypted_char
                else:
                    decrypted_message += char
            print(f"Shift {shift}: {decrypted_message}")

    def get_input(self) -> None:
        while True:
            blank_string = str(input("Enter string to decrypt: "))
            blank_string = blank_string.lower()
            self.blank_string = blank_string
            break

    def encrypt_string(self) -> str:
        output = ""
        for c in self.blank_string:
            for k, v in self.key.items():
                if k == c:
                    output += v
                else:
                    continue
        self.decrypted_string = output
        return (output)

    def decrypt_string(self, string: str) -> str:
        output = ""
        string = string.lower()
        string = string.strip()
        if string == "":
            return (self.blank_string)
        else:
            for c in string:
                for k, v in self.key.items():
                    if v == c:
                        output += k

        return (output)


if __name__ == "__main__":
    key = {"1": "5", "2": "6", "3": "7", "4": "8", "5": "9", "6": "1", "7": "2", "8": "3", "9": "4", " ": "$", "a": "e", "b": "f", "c": "g", "d": "h", "e": "i", "f": "j", "g": "k", "h": "l", "i": "m", "j": "n", "k": "o", "l": "p", "m": "q",
           "n": "r", "o": "s", "p": "t", "q": "u", "r": "v", "s": "w", "t": "x", "u": "y", "v": "z", "w": "a", "x": "b", "y": "c", "z": "d"}
    # key = {"a": "e", "b": "f", "c": "g", "d": "h", "e": "i", "f": "j", "g": "k", "h": "l", "i": "m", "j": "n", "k": "o", "l": "p", "m": "q",
    #    "n": "r", "o": "s", "p": "t", "q": "u", "r": "v", "s": "w", "t": "x", "u": "y", "v": "z", "w": "a", "x": "b", "y": "c", "z": "d"}
    main_instance = main(key=key)
    main_instance.get_input()
    print(main_instance.encrypt_string())
    # ciphertext = main_instance.encrypt_string()
    # main_instance.decrypt_caesar(ciphertext)
