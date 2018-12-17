from random import randint
from cipher.TripleDES import *


class TimeLockPuzzle():

    def __init__(self, T=10, S=5):

        '''
        :param T: number of seconds for time lock puzzle
        :param S: expected number of squarings modulo n per second that can be performed by solver
        '''

        self.T = T
        self.S = S
        self.triple_des = TripleDES()

        pass

    def is_prime(self, num, test_count):
        if num == 1:
            return False
        if test_count >= num:
            test_count = num - 1
        for x in range(test_count):
            val = randint(1, num - 1)
            if pow(val, num - 1, num) != 1:
                return False
        return True

    def generate_big_prime(self, n, test_count=1000):
        found_prime = False
        while not found_prime:
            p = randint(2 ** (n - 1), 2 ** n)
            if self.is_prime(p, test_count):
                return p

    def generate_puzzle(self, m):

        '''
        :param m: message
        :return: (n, a, t, Ck, Cm) - like in paper http://people.csail.mit.edu/rivest/RivestShamirWagner-timelock.pdf
        '''

        p = self.generate_big_prime(20)
        q = self.generate_big_prime(20)
        n = p * q
        phi_n = (p - 1) * (q - 1)

        t = self.T * self.S  # difficulty

        Cm = self.triple_des.encode(m)  # encoded message
        K = Cm[1] + Cm[2] + Cm[3]  # key
        Cm = Cm[0][1]  # message without key info
        K = acsii_to_binary(K)
        K = int(K, 2)

        a = 2
        e = pow(2, t, phi_n)
        b = pow(a, e, n)
        Ck = K + b  # puzzle

        return n, a, t, Ck, Cm

    def solve_puzzle(self, n, a, t, Ck, Cm):

        '''
        :param n, a, t, Ck, Cm: from generate_puzzle
        :return: decrypted message
        '''

        b = a
        for i in range(t):
            b = pow(b, 2, n)

        K = Ck - b
        K = bin(K).replace("b", "")
        K = binary_to_acsii(K)
        decrypted_m = self.triple_des.decode(Cm, K[:7], K[7:14], K[14:])

        return decrypted_m
