import base64
from Crypto.Cipher import AES # requires pycryptodome

def grabBytes(filename):
    f = open(filename, "r")
    contents = f.read()
    f.close()
    contents.replace("\n", "")
    return base64.b64decode(contents)

def repeatKeyXor(inputBytes, key):
    outputBytes = b""
    for i, byte in enumerate(inputBytes):
        position = i % len(key)
        outputBytes += bytes([byte ^ key[position]])
    return outputBytes

def split(inputBytes, length):
    outputList = []
    for i in range(0, len(inputBytes), length):
        outputList.append(inputBytes[i : i + length])
    return outputList

def repeatKeyXorList(bytesList, key):
    decodedBlocks = map(lambda x : repeatKeyXor(x, key), bytesList)

    outputBytes = b""
    for block in decodedBlocks:
        outputBytes += block
    return outputBytes

def aes128ecb(inputBytes, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(inputBytes)
    return plaintext

if __name__ == "__main__":
    data = grabBytes("7.txt")
    key = b"YELLOW SUBMARINE"

    plaintext = aes128ecb(data, key)
    print(plaintext.decode())
