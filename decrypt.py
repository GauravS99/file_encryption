from cryptography.fernet import Fernet

cipher_text = ""
with open("./file/encrypted", 'rb') as readFile:
    cipher_text = readFile.read()

key = ""
with open("key.txt", 'rb') as keyFile:
    key = keyFile.read()

cipher_suite = Fernet(key)

plain_text = cipher_suite.decrypt(cipher_text)

with open("./output/decrypted", 'wb') as writeFile:
    writeFile.write(plain_text)