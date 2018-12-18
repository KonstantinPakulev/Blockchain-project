from cipher.TripleDES import *
from puzzle.puzzle import TimeLockPuzzle

triple_des = TripleDES()

string_to_encode = "0123456789ABCDEF"
encoded = triple_des.encode("0123456789ABCDEF")
# Tuple consisting of encoded text, its binary representation and three keys
print(encoded)
print("Key:", encoded[1] + encoded[2] + encoded[3])

decoded = triple_des.decode(encoded[0][1], encoded[1], encoded[2], encoded[3])
# Decoded text and its binary representation
print(decoded)

# Check puzzle
T = 5 # sec
tlp = TimeLockPuzzle(T)
n, a, t, Ck, Cm, K, b, phi_n = tlp.generate_puzzle(string_to_encode)

solution, key, decrypted_message = tlp.solve_puzzle(n, a, t, Ck, Cm)
print("Sequential:")
print(solution)
print(key)
print(decrypted_message)

solution_trap, key_trap, decrypted_message_trap = tlp.solve_puzzle_via_trapdoor(n, a, t, Ck, Cm, phi_n)
print("Trap:")
print(solution_trap)
print(key_trap)
print(decrypted_message_trap)

T = 1  # sec
tlp = TimeLockPuzzle(T)
n, a, t, Ck, Cm = tlp.generate_puzzle(string_to_encode)
decrypted_message = tlp.solve_puzzle(n, a, t, Ck, Cm)
print(decrypted_message)
