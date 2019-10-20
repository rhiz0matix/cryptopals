from challenge7 import aes128ecb
from challenge3 import charFreqScore
from challenge6 import bestKeySize, splitBytes, transpose, keySizeScore
from itertools import product

def grabByteList(filename):
    f = open(filename, "r")
    bytelist = []

    for line in f: # Unsure if strips newlines
        bytelist.append(bytes.fromhex(line))

    f.close()
    return bytelist

def aesSingleCharBrute(inputBytes):
    bestScore = -1
    bestDecipher = b""
    bestChar = -1

    newinput = inputBytes
    while len(newinput) % 16 != 0:
        newinput += b"\x04"

    for c in range(256):
        key = bytes([c] * 16)
        candidateBytes = aes128ecb(newinput, key)
        score = charFreqScore(candidateBytes)

        if score > bestScore:
            bestScore = score
            bestDecipher = candidateBytes
            bestChar = c
    return [bestDecipher, bestChar, bestScore]

def aesBrute(inputBytes):
    keys = product(range(256), repeat = 16)

    bestKey = b""
    bestScore = -1
    bestDecipher = b""
    for key in keys:
        bytesKey = bytes(key)
        decipher = aes128ecb(inputBytes, bytesKey)
        score = charFreqScore(decipher)

        if score > bestScore:
            bestKey = bytesKey
            bestScore = score
            bestDecipher = decipher
    return (bestKey, bestScore, bestDecipher)

def freqCounter(inputBytes):
    counter = {}
    for byte in inputBytes:
        if byte in counter:
            counter[byte] += 1
        else:
            counter[byte] = 1
    return counter

if __name__ == "__main__":
    bytelist = grabByteList("8.txt")
    keySize = 16

    bestScore = 1024
    bestLine = b""
    for line in bytelist:
        score = keySizeScore(line, keySize)
        if score < bestScore:
            bestScore = score
            bestLine = line

    print(len(bestLine))
    splitLine = splitBytes(bestLine, keySize)
    transposeLine = transpose(splitLine, keySize)
    key = b""
    for chunk in transposeLine:
        d, c, s = aesSingleCharBrute(chunk)
        key += bytes([c])

    freqs = freqCounter(bestLine)
    sortedFreqs = sorted([(freqs[b], b) for b in freqs])
    #print(sortedFreqs)
    print(bestLine)
    #print(key)
    #print(aes128ecb(bestLine, key))
