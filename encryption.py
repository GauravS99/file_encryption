from cryptography.fernet import Fernet

payload = ""
with(open("./file/file", "rb")) as readFile:
    payload = readFile.read();

cipher_text = cipher_suite.encrypt(payload)

with open("encrypted.txt", 'wb') as writeFile:
    writeFile.write(cipher_text)

plain_text = cipher_suite.decrypt(cipher_text)

with open("decrypted.txt", 'wb') as writeFile:
    writeFile.write(plain_text)
