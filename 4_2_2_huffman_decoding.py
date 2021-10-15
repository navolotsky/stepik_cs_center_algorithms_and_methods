def huffman_decoding(char_codes, s):
    left = s
    result = ""
    while left:
        for char, code in char_codes.items():
            if left.startswith(code):
                result += char
                left = left[len(code):]
                break
        else:
            raise ValueError(
                'Cannot decode given string using given codes table.')
    return result


def main():
    k, _ = map(int, input().split())
    char_codes = {}
    for _ in range(k):
        char, code = input().split(': ')
        char_codes[char] = code
    encoded_string = input()
    decoded_string = huffman_decoding(char_codes, encoded_string)
    print(decoded_string)


if __name__ == "__main__":
    main()
