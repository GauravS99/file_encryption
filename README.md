# General Setup

Install requirements in requirements.txt by running 
```
pip install -r requirements.txt
```

you should probably do this in a virtual environment

# How to encrypt

1. Generate a key by running 

```
python generate_key.py
```
You will need to somehow share this key with anybody who needs to decrypt

2. Place the file you want to encrypt in the "file" folder with the name "file" (no extension)
3. Run 
```
python encrypt.py
```
4. Find the encrypted file in the output folder..

# How to decrypt

1. Aquire the key from person encrypting, and create a text file with this key called "key.txt" in
the root folder

2 Aquire the file that needs to be encrypted. Rename it to "encrypted". Place it in the "file" folder. 

3. Run 
```
python decrypt.py
```
4. you can find the file in the output folder. Rename it to the extension it was originally to acces it




