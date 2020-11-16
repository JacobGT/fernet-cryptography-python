from cryptography.fernet import Fernet #Imports the cryptography package and fernet which will encrypt
# We save the generated key in a variable
key = Fernet.generate_key()
# Creates a byte document with write byte permission
file = open("key.key", "wb")
# Write the key to file
file.write(key)
# Close file
file.close()
# Check the link below to see the real pro tutorial
# https://youtu.be/H8t4DJ3Tdrg
