# Function to decode hex-encoded characters
def decode_hex(match):
    return chr(int(match.group(0)[1:], 16))