from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open("key.txt", 'wb') as writeFile:
    writeFile.write(key)
