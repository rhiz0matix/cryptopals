def repeatingKeyXor(inputBytes, key):
    """Applies repeating-key XOR to inputBytes with key. Assumes key
    is a bytes type object."""

    outputBytes = b""
    i = 0
    for byte in inputBytes:
        position = i % len(key)
        outputBytes += bytes([byte ^ key[position]])
        i += 1
    return outputBytes

if __name__ == "__main__":
    cipherText = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    key = b"ICE"

    encoded = repeatingKeyXor(cipherText, key)
    print(bytes.hex(encoded))
