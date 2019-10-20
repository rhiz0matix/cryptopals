import base64

def parseHex(s):
    """Converts string s from hexidecimal to bytes object."""

    return bytes.fromhex(s)

def convertBase64(b):
    """Encodes a bytes object in base 64."""
    return base64.b64encode(b)

if __name__ == "__main__":
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    data = parseHex(s)
    print(convertBase64(data).decode())
