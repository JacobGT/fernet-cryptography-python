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

# Encode message
message = "My deep dark secret."
encoded_message = message.encode()

# Encrypt message
f = Fernet(key)
encrypted_message = f.encrypt(encoded_message)

# Save message to file
file = open("encryptedMessage.byte", "wb")
file.write(encrypted_message)  # Also is in bytes
file.close()
