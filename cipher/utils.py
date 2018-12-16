def split(string, length):
    return [string[i:i + length] for i in range(0, len(string), length)]


def permutation(bytes, order):
    result = list("x" * len(order))

    for index, i in enumerate(order):
        result[index] = bytes[i]

    return "".join(result)


def acsii_to_binary(acsii_string):
    binary_text = ""
    for i in acsii_string:
        # convert to ASCII binary and pad with zeros
        binary_text += format(ord(i), "08b")

    return binary_text


def binary_to_acsii(binary_string):
    bytes = split(binary_string, 8)
    chars = ""

    for i in bytes:
        chars += chr(int(i, 2))

    return chars


def binary_to_hex(binary_string):
    return '%0*X' % ((len(binary_string) + 3) // 4, int(binary_string, 2))
