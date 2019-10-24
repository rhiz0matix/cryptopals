import sys
sys.path.insert(1, "../set1")
from challenge7 import aes128ecb_dec
from challenge9 import pkcs7pad
from challenge2 import xor
import base64
from Crypto.Cipher import AES

def aes128ecb_enc(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def cbc_enc(inputBytes, iv, key):
    blocksize = 16
    if len(iv) != blocksize:
        raise ValueError

    ciphertext = b""
    prevBlock = iv
    for i in range(0, len(inputBytes), blocksize):
        nextBlock = inputBytes[i : i + blocksize]
        a = xor(nextBlock, prevBlock)
        print(a)
        prevBlock = aes128ecb_enc(a, key)
        ciphertext += prevBlock

    return ciphertext

def cbc_dec(ciphertext, iv, key):
    blocksize = 16
    if len(iv) != blocksize:
        raise ValueError
    
    plaintext = b""
    prevBlock = iv
    for i in range(0, len(ciphertext), blocksize):
        decBlock = aes128ecb_dec(ciphertext[i : i + blocksize], key)
        plaintext += xor(prevBlock, decBlock)
        prevBlock = ciphertext[i : i + blocksize]

    return plaintext

def michaelCypherTest():
    plaintext = pkcs7pad(b"Hello my name is Michael", 16)
    iv = bytes([0]) * 16
    key = "YELLOW SUBMARINE"

    enc = cbc_enc(plaintext, iv, key)
    print(enc)
    print(cbc_dec(end, iv, key))

if __name__ == "__main__":
    michaelCypherTest()
    #print(aes128ecb_enc(b"1234567890123456", b"YELLOW SUBMARINE"))
    #f = open("10.txt", "r")
    #data = base64.b64decode(f.read().replace("\n", ""))
    #f.close()

    #key = b"YELLOW SUBMARINE"
    #iv = bytes([0]) * 16
    #print(cbc_dec(data, iv, key).decode())
