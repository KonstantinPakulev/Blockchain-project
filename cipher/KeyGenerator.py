from cipher.utils import *


class KeyGenerator:

    def __init__(self, key):
        assert len(key) == 7

        binary_key = acsii_to_binary(key)

        extended_binary_key = ""
        # Extend key to 64 bits
        for i in range(0, len(binary_key) + 1, 8):
            byte = binary_key[i:i + 8]
            extended_binary_key += byte
            if byte.count('1') % 2 == 0:
                extended_binary_key += '1'
            else:
                extended_binary_key += '0'

        c0_permutation = [56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17,
                          9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35]

        d0_permutation = [62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21,
                          13, 5, 60, 52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3]

        c = permutation(extended_binary_key, c0_permutation)
        d = permutation(extended_binary_key, d0_permutation)

        shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        key_permutation = [13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3, 25, 7, 15, 6, 26, 19, 12, 1, 40,
                           51,
                           30, 36, 46, 54, 29, 39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]

        self.keys = []

        for i in range(0, 16):
            c = shift(c, shift_table[i])
            d = shift(d, shift_table[i])

            self.keys.append(permutation(c + d, key_permutation))

    def get_key(self, i):
        return self.keys[i]


def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]
