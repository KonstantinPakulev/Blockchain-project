from cipher.TripleDES import *

triple_des = TripleDES()

string_to_encode = "0123456789ABCDEF"
encoded = triple_des.encode("0123456789ABCDEF")
# Tuple consisting of encoded text, its binary representation and three keys
print(encoded)
print("Key:", encoded[1] + encoded[2] + encoded[3])

decoded = triple_des.decode(encoded[0][1], encoded[1], encoded[2], encoded[3])
# Decoded text and its binary representation
print(decoded)
