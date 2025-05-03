import sys
from hashlib import blake2s

SALT = b">rb<"

if len(sys.argv) != 3:
    print("Encryption Usage: python3 hashbrown.py enc <filename>")
    print("Decryption Usage: python3 hashbrown.py dec <filename>")
    sys.exit(1)

def encrypt(filename):
    with open(filename, "rb") as f:
        buf0 = f.read()
        buf1 = [buf0[i:i+2] for i in range(0, len(buf0), 2)]
        if len(buf1[-1]) == 1: buf1[-1] += b" "
        buf2 = [SALT + i for i in buf1]
        buf3 = [blake2s(i).hexdigest() for i in buf2]
        open(filename + ".enc", "w").write("\n".join(buf3))
    print(f"Encryption completed: {filename}.enc")

def decrypt(filename):
    #      _                                                           _                _                      _
    #     | |      _                                              _   (_)              | |                    | |
    #   _ | | ____| |_  ____     ____ ___   ____ ____ _   _ ____ | |_  _  ___  ____    | | _   ____  ____ ____| |
    #  / || |/ _  |  _)/ _  |   / ___) _ \ / ___) ___) | | |  _ \|  _)| |/ _ \|  _ \   | || \ / _  )/ ___) _  )_|
    # ( (_| ( ( | | |_( ( | |  ( (__| |_| | |  | |   | |_| | | | | |__| | |_| | | | |  | | | ( (/ /| |  ( (/ / _
    #  \____|\_||_|\___)_||_|   \____)___/|_|  |_|    \____| ||_/ \___)_|\___/|_| |_|  |_| |_|\____)_|   \____)_|
    #                                                      |_|
    print(f"Decryption completed: {filename}.dec")

match sys.argv[1]:
    case "enc": encrypt(sys.argv[2])
    case "dec": decrypt(sys.argv[2])
    case _: print(f"Invalid option: {sys.argv[1]}")
