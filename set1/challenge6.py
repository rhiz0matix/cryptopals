import base64
from challenge3 import charFreqScore, singleCharXor
from challenge5 import repeatingKeyXor

def oneCounter(n):
    """Computes the number of ones in the binary representation
    of the integer n."""
    if n == 0:
        return 0

    return (1 & n) + oneCounter(n >> 1)

def binEditDistance(b1, b2):
    """Returns the edit distance between two bytes objects."""
    if len(b1) > len(b2):
        return binEditDistance(b2, b1)

    numOfOnes = 0
    for i in range(len(b1)):
        numOfOnes += oneCounter(b1[i] ^ b2[i])

    for byte in b2[len(b1):]:
        numOfOnes += oneCounter(byte)

    return numOfOnes

def keySizeScore(inputBytes, keySize, n=1):
    """Scores a keySize from the ciphertext inputBytes using the first n chucks of length keySize."""
    #total = sum([binEditDistance(inputBytes[keySize * i : keySize * (i + 1)], inputBytes[keySize * (i + 1) : keySize * (i + 2)]) for i in range(n)])
    total = 0
    for i in range(n):
        total += binEditDistance(inputBytes[keySize * i : keySize * (i + 1)], inputBytes[keySize * (i + 1) : keySize * (i + 2)])
    #return total / (n * keySize) 
    return total / (keySize) 

#def bestKeySize(inputBytes, lo, hi):
#    bestScore = hi + 1
#    bestSize = hi + 1
#    for size in range(lo, hi + 1):
#        score = keySizeScore(inputBytes, size)
#        if score < bestScore:
#            bestScore = score
#            bestSize = size
#    return bestSize

def bestKeySizes(inputBytes, lo, hi):
    scores = set()
    for size in range(lo, hi + 1):
        scores.add((keySizeScore(inputBytes, size), size))
    return scores

def grabBytes(filename):
    """Returns the contents of the file in a byte array. Assumes the file contents
    is encoded in base 64."""

    f = open(filename, "r")
    contents = f.read()
    f.close()
    contents.replace("\n", "")
    return base64.b64decode(contents)

def decipherSingleCharXor(inputBytes):
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
    """Returns a list of bytes objects."""
    outputList = []
    for i in range(0, len(inputBytes), length):
        outputList.append(inputBytes[i : i + length])
    return outputList

def transpose(bytesList, length):
    outputList = []
    for i in range(length):
        outputList.append(b"")
        for inputBytes in bytesList:
            if i < len(inputBytes):
                outputList[i] += bytes([inputBytes[i]])
    return outputList

if __name__ == "__main__":
    data = grabBytes("6.txt")

    #keySize = bestKeySize(data, 2, 40)
    keySizes = bestKeySizes(data, 2, 40)

    #test = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    #(d, c) = decipherSingleCharXor(test)
    #print(c)

    #test = splitBytes(b"This is a test of the split bytes function!", 3)
    #print(transpose(test, 3))

    keySize = 29 # TODO Fix keySize computation
    splitData = splitBytes(data, keySize)
    transData = transpose(splitData, keySize)
    key = b""
    for inputBytes in transData:
        (d, c) = decipherSingleCharXor(inputBytes)
        key += chr(c).encode()
    print(key)

    deciphered = repeatingKeyXor(data, key)
    print(deciphered.decode())


   # i = 0
   # keys = []
   # for score, keySize in keySizes:
   #     if i == 5:
   #         break
   #     i += 1

   #     splitData = splitBytes(data, keySize)
   #     transData = transpose(splitData, keySize)

   #     key = b""
   #     for inputBytes in transData:
   #         (d, c) = decipherSingleCharXor(inputBytes)
   #         key += chr(c).encode()
   #     keys.append(key)

   # #print(keys)
   # decipheredList = []
   # for key in keys:
   #     deciphered = repeatingKeyXor(data, key)
   #     decipheredList.append(deciphered)
   # print(decipheredList[3])




    #splitData = splitBytes(data, keySize)
    #transData = transpose(splitData, keySize)

    #key = ""
    #for inputBytes in transData:
    #    (d, c) = decipherSingleCharXor(inputBytes)
    #    key += (chr(c))
    #    print(inputBytes)
    #    print(c)
#    print(key)
#    print(data[:2 * keySize])
#    print(splitData[0])
#    print(splitData[1])
#    print(splitData[2])
#    print(transData[0])
