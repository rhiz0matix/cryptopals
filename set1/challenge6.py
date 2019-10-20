import base64
from challenge3 import charFreqScore, singleCharXor
from challenge5 import repeatingKeyXor

"""Attempts to break repeating key XOR in a text document.
Cryptopals set 1 challenge 6.
Last modified: October 17, 2019."""

def oneCounter(n):
    """Computes the number of ones in the binary representation
    of the integer n."""
    if n == 0:
        return 0

    return (1 & n) + oneCounter(n >> 1)

def binEditDistance(b1, b2):
    """Returns the binary edit distance between two bytes objects."""
    if len(b1) > len(b2):
        return binEditDistance(b2, b1)

    # the number of ones in b1 ^ b2 is the binary edit distance
    numOfOnes = 0
    for i, b in enumerate(b1):
        numOfOnes += oneCounter(b ^ b2[i])

    for byte in b2[len(b1):]:
        numOfOnes += oneCounter(byte)

    return numOfOnes

def keySizeScore(inputBytes, keySize):
    """Scores a keySize from the ciphertext inputBytes length keySize chunks from inputBytes."""
    chunks = splitBytes(inputBytes, keySize)
    averages = []
    for i in range(0, len(chunks), 2):
        if i + 1 < len(chunks):
            averages.append(binEditDistance(chunks[i], chunks[i + 1]) / keySize)
    return sum(averages) / len(averages)

def bestKeySize(inputBytes, lo, hi):
    """Returns the best key size in range lo to hi (inclusive)."""
    bestScore = hi + 1
    bestSize = hi + 1
    for size in range(lo, hi + 1):
        score = keySizeScore(inputBytes, size)
        if score < bestScore:
            bestScore = score
            bestSize = size
    return bestSize

def keySizes(inputBytes, lo, hi):
    """Returns a set of tuples (score, keySize) of key sizes."""
    scores = set()
    for size in range(lo, hi + 1):
        scores.add((keySizeScore(inputBytes, size), size))
    return scores

def grabBytes(filename):
    """Returns the contents of the file in bytes object. Assumes the file contents
    is encoded in base 64."""

    f = open(filename, "r")
    contents = f.read()
    f.close()
    contents.replace("\n", "")
    return base64.b64decode(contents)

def decipherSingleCharXor(inputBytes):
    """Attempts to brute force decipher inputBytes using single character XOR and English
    character frequencies."""
    bestScore = -1
    bestChar = 0
    bestDecipher = b""

    for c in range(256):
        xored = singleCharXor(inputBytes, c)
        score = charFreqScore(xored)

        if score > bestScore:
            bestScore = score
            bestDecipher = xored
            bestChar = c

    return (bestDecipher, bestChar)

def splitBytes(inputBytes, length):
    """Splits inputBytes into a list of bytes objects. Each bytes object in the list
    is of size length."""
    outputList = []
    for i in range(0, len(inputBytes), length):
        outputList.append(inputBytes[i : i + length])
    return outputList

def transpose(bytesList, length):
    """Transposes a list of bytes."""
    outputList = []
    for i in range(length):
        outputList.append(b"")
        for inputBytes in bytesList:
            if i < len(inputBytes):
                outputList[i] += bytes([inputBytes[i]])
    return outputList

if __name__ == "__main__":
    data = grabBytes("6.txt")
    keySize = bestKeySize(data, 2, 40)
    
    splitData = splitBytes(data, keySize)
    transData = transpose(splitData, keySize)

    key = b""
    for inputBytes in transData:
        (d, c) = decipherSingleCharXor(inputBytes)
        key += chr(c).encode()
    print("This is the key:")
    print(key.decode())

    deciphered = repeatingKeyXor(data, key)
    print("\nThis is the deciphered text:")
    print(deciphered.decode())
