import json

def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key, ciphertext):
    S = KSA(key)
    keystream = PRGA(S)
    plaintext = []
    for byte in ciphertext:
        plaintext_byte = byte ^ next(keystream)
        plaintext.append(plaintext_byte)
    return bytes(plaintext)

def main():
    result = ""
    key = 'Armin'
    ciphertext_json = input()
    
    # Parse JSON string
    ciphertext_data = json.loads(ciphertext_json)
    ciphertext = bytes(ciphertext_data["data"])

    plaintext = RC4(key.encode(), ciphertext)
    result= plaintext.decode()

    # Output result as JSON
    print(result)

if __name__ == "__main__":
    main()
