from challenge3 import charFreqScore
from challenge3 import topDecipher

def fileDecipher(filename):
    """Returns a list of the best deciphered string in file.
    The list consists of entries in the form (bytes, score)."""

    f = open(filename, "r")
    fl = f.readlines()

    bestStrings = []
    for line in fl:
        inputBytes = bytes.fromhex(line.rstrip("\n"))
        bestStrings.append(topDecipher(inputBytes))

    f.close()
    return bestStrings

if __name__ == "__main__":
    bests = fileDecipher("4.txt")
    bestScore = -1
    bestBytes = b""
    for (bs, score) in bests:
        if score > bestScore:
            bestScore = score
            bestString = bs
    print(bestScore, bestString.decode())
