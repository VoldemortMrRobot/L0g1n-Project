from cryptography.fernet import Fernet
def load_key():
	return open ("secret.key", "rb").read()
	
def decrypt_data(encrypted_data,key):
	fernet = Fernet(key)
	decrypted_data = fernet.decrypt(encrypted_data).decode()
	return decrypted_data
# Load the key and decrypt the file

key = load_key()
with open('pw.txt', 'rb') as file:
	encrypted_data = file.read()
decrypted_data = decrypt_data(encrypted_data, key)
print("Decrypted data: ", decrypted_data)
