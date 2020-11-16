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

# Open the file to decrypt
with open("exampleText.txt.encrypted", "rb") as f:
    data = f.read()

fernet = Fernet(key)
decrypted_file = fernet.decrypt(data)

# Write the decrypted data to a new file
with open("exampleText.txt.decrypted", "wb") as f:
    f.write(decrypted_file)

