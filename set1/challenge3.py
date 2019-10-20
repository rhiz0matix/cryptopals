import binascii
import base64

def singleCharXor(inputBytes, c):
    """Performs xor against byte c on each entry of inputBytes."""
    #return bytes(map(lambda x: x ^ c, arr))
    output = b""
    for byte in inputBytes:
        output += bytes([byte ^ c])
    return output

# English character frequency according to Wikipedia
freqTable = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.36,
    "x": 0.15,
    "y": 1.974,
    "z": 0.074,
    " ": 13
}

def charFreqScore(inputBytes, table = freqTable):
    """Scores a string s according to table, which records character frequencies."""
    score = 0
    for byte in inputBytes:
        c = chr(byte).lower()
        if c in table:
            score += table[c]
    return score

def decipherSingleCharXor(inputBytes):
    """Returns an ordered list of tuples (bytes, score) of candidate
    deciphered versions of hexString. The cipher is assumed to be
    XOR with a single byte character. Highest scoring strings appear
    first."""

    scores = {}

    for c in range(256):
        xored = singleCharXor(inputBytes, c)
        score = charFreqScore(xored)

        scores[xored] = score

    sortedScores = [(s, scores[s]) for s in sorted(scores, key=scores.get, reverse=True)]
    return sortedScores

def topDecipher(inputBytes):
    """Returns the top result of deciphering inputBytes in the form
    (bytes, score)."""

    candidates = decipherSingleCharXor(inputBytes)
    return candidates[0]

if __name__ == "__main__":
    hexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    (bs, score) = topDecipher(bytes.fromhex(hexString))
    print(bs.decode())
