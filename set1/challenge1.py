import string

def parseHex(s):
    return int(s, base=16)

def convertBase64(n):
    baseTable = string.ascii_uppercase + string.ascii_lowercase + "0123456789+/"

    if n < 64:
        return baseTable[n]
   
    return convertBase64(n // 64) + baseTable[n % 64]

if __name__ == "__main__":
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    hexed = parseHex(s)
    print(convertBase64(hexed))
