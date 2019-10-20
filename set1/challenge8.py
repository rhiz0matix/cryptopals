def grabByteList(filename):
    f = open(filename, "r")
    bytelist = []

    for line in f:
        bytelist.append(bytes.fromhex(line))

    f.close()
    return bytelist

def countRepeatChunks(inputBytes, length):
    """Returns the number of most repeats chunks of size length in inputBytes."""
    chunks = [inputBytes[i : i + length] for i in range(0, len(inputBytes), length)]
    chunks = sorted(chunks)
    
    mostRepeats = 0
    prevIndex = 0 # Index of first instance of previously seen chunk
    for i, chunk in enumerate(chunks):
        repeats = 0
        if chunks[prevIndex] != chunk:
            repeats = i - prevIndex
            prevIndex = i

            if repeats > mostRepeats:
                mostRepeats = repeats
    return mostRepeats

if __name__ == "__main__":
    bytelist = grabByteList("8.txt")
    keySize = 16

    mostChunks = 0
    bestLine = b""
    for line in bytelist:
        count = countRepeatChunks(line, keySize)
        if count > mostChunks:
            mostChunks = count
            bestLine = line

    print(bytes.hex(bestLine))
