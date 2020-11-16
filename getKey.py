from cryptography.fernet import Fernet #Imports the cryptography package and fernet which will encrypt
# Open a byte document with read byte permission
file = open("key.key", "rb")
# Reads the key and writes it to a variable
key = file.read()
# Close file
file.close()
# Shows key
print(key)
