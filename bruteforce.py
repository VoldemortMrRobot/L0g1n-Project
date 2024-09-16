import hashlib
def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()
	
def load_dictionary(file_path,encoding='utf-8'):
	dictionary = []
	with open(file_path, 'rb') as file:
		for line in file:
			try:
				line = line.decode(encoding).strip()
				dictionary.append(line)
			except UnicodeDecodeError:
				#Handle or log the decoding error if needed
				continue
	return dictionary

def dictionary_attack(stored_hash,dictionary):
	for password in dictionary:
		if hash_password(password) == stored_hash:
			return password
	return None

#Hashes from the decrypted data
a = input("Enter the decrypted hash you want to crack 🙂: ")
stored_hash = a

# Load dictionary file
dictionary_file = 'rockyou.txt'
dictionary = load_dictionary(dictionary_file)

# Perform dictionary attack

password = dictionary_attack(stored_hash, dictionary)
if password:
	print(f"Password found: {password}")
else:
	print("Password not found!")

