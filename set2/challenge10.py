import sys
sys.path.insert(1, "../set1")
from challenge7 import aes128ecb
from challenge9 import pkcs7pad
import base64

def cbc(inputBytes, iv, key):
    ciphertext = iv
    blocksize = 16

    padIndex = blocksize - (len(ciphertext) % blocksize)
    ciphertext += inputBytes[:padIndex]
    ciphertext = aes128ecb(ciphertext, key)

    while padIndex + blocksize < len(inputBytes):
        ciphertext += inputBytes[padIndex : padIndex + blocksize]
        ciphertext = aes128ecb(ciphertext, key)
        padIndex += blocksize

    ciphertext += inputBytes[padIndex :]
    ciphertext = pkcs7pad(ciphertext, blocksize)
    ciphertext = aes128ecb(ciphertext, key)
    return ciphertext

if __name__ == "__main__":
    f = open("10.txt", "r")
    data = base64.b64decode(f.read())
    f.close()

    key = b"YELLOW SUBMARINE"
    iv = b"\x00\x00\x00 &c"
    print(cbc(data, iv, key))
