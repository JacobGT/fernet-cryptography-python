from cryptography.fernet import Fernet
# Generate key / (If key has all ready been generated skip this step)
key = Fernet.generate_key()
file = open("key.key", "wb")
file.write(key)
file.close()

# Read key / Get the key from the file
file = open("key.key", "rb")
key = file.read()  # The key will be type 'bytes'
file.close()

# Read encrypted message and save it to variable
file = open("encryptedMessage.byte", "rb")
encrypted_message = file.read()  # Also is in bytes
file.close()

# Decrypt the encrypted message
f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message)

# To know that the variable is as byte it with show like this: b'blahblahblah'
# To decode the byte to string

# Decode the encoded message
original_message = decrypted_message.decode()

# Show original message
print(original_message)
