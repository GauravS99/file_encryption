from cryptography.fernet import Fernet

key = ""
with open("key.txt", 'rb') as keyFile:
    key = keyFile.read()

cipher_suite = Fernet(key)

payload = ""
with(open("./file/file", "rb")) as readFile:
    payload = readFile.read()

cipher_text = cipher_suite.encrypt(payload)

with open("./output/encrypted", 'wb') as writeFile:
    writeFile.write(cipher_text)