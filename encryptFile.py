from cryptography.fernet import Fernet

# Create file to demonstrate
key = Fernet.generate_key()
file = open("exampleText.txt", "w")
file.write("Deep dark secret BUT this time it is in a .txt file.")
file.close()

# Generate key / (If key has all ready been generated skip this step)
key = Fernet.generate_key()
file = open("key.key", "wb")
file.write(key)
file.close()

# Read key / Get the key from the file
file = open("key.key", "rb")
key = file.read()  # The key will be type 'bytes'
file.close()

# Open the file to encrypt
with open("exampleText.txt", "rb") as f:
    data = f.read()

fernet = Fernet(key)
encrypted_file = fernet.encrypt(data)

# Write the encrypted data to a new file
with open("exampleText.txt.encrypted", "wb") as f:
    f.write(encrypted_file)

