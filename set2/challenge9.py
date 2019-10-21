def pkcs7pad(inputBytes, blocksize):
    padByte = bytes([blocksize - (len(inputBytes) % blocksize)])
    while len(inputBytes) % blocksize != 0:
        inputBytes += padByte
    return inputBytes

if __name__ == "__main__":
    test = b"YELLOW SUBMARINE"
    print(pkcs7pad(test, 20))
