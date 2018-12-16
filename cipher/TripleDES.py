from cipher.DES import *
from random import choice
from string import ascii_letters, digits


def generate_key():
    return ''.join(choice(ascii_letters + digits) for i in range(7))


class TripleDES:
    def __init__(self):
        pass

    def encode(self, text):
        k1 = generate_key()
        k2 = generate_key()
        k3 = generate_key()

        des = DES()

        Ek1 = des.encode(text, k1)
        Dk2 = des.decode(Ek1[1], k2)
        Ek3 = des.encode(Dk2[1], k3)

        return Ek3, k1, k2, k3

    def decode(self, text, k1, k2, k3):
        des = DES()

        Dk3 = des.decode(text, k3)
        Ek2 = des.encode(Dk3[1], k2)
        Dk1 = des.decode(Ek2[1], k1)

        return Dk1
