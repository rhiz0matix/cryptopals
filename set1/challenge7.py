import base64
from Crypto.Cipher import AES # requires pycryptodome

def grabBytes(filename):
    f = open(filename, "r")
    contents = f.read()
    f.close()
    contents.replace("\n", "")
    return base64.b64decode(contents)

def aes128ecb_dec(inputBytes, key):
    """Decrypts inputBytes using key with the AES-128 ECB algorithm."""
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(inputBytes)
    return plaintext

if __name__ == "__main__":
    data = grabBytes("7.txt")
    key = b"YELLOW SUBMARINE"

    plaintext = aes128ecb(data, key)
    print(plaintext.decode())
