from challenge1v2 import parseHex
from challenge1v2 import convertBase64
import binascii

def xor(arr1, arr2):
    """Takes XOR of two byte arrays."""
    return bytes(map(lambda x, y: x ^ y, arr1, arr2))

if __name__ == "__main__":
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    
    data1 = parseHex(s1)
    data2 = parseHex(s2)
    xored = xor(data1, data2)
    hexed = binascii.b2a_hex(xored)
    print(hexed.decode())
