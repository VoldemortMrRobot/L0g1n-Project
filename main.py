from cryptography.fernet import Fernet
import hashlib
import webbrowser

# Generate a key for encryption (store this securely in a real application)
# You can generate and store this key separately to reuse it.

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the data using the key
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt the data using the key
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Function to hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Store the hashed password encrypted in pw.txt
def store_password(username, password):
    key = load_key()
    hashed_password = hash_password(password)
    data = f"{username}:{hashed_password}"

    encrypted_data = encrypt_data(data, key)
    with open('pw.txt', 'wb') as f:
        f.write(encrypted_data)
    print("Password stored securely!")

# Verify the entered password
def verify_password(username, password):
    key = load_key()
    hashed_password = hash_password(password)

    try:
        with open('pw.txt', 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = decrypt_data(encrypted_data, key)
        stored_username, stored_hashed_password = decrypted_data.split(':')

        if stored_username == username and stored_hashed_password == hashed_password:
            print("Very well! Welcome! " + stored_username)
            print("Here are your options: ")
            print("")
            print("1. See the code")
            print("2. See the author")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                webbrowser.open("https://github.com/VoldemortMrRobot/L0g1n-Project/blob/main/main.py")
            elif choice == "2":
                webbrowser.open("https://github.com/VoldemortMrRobot")
            elif choice == "3":
                print("Exiting...")
            else:
                print("Invalid choice!")
        else:
            print("Incorrect username or password!")
    except FileNotFoundError:
        print("No password found, please register first.")

# Main program
def main():
    choice = input("Do you want to (1) register or (2) login? ")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if choice == "1":
        store_password(username, password)
    elif choice == "2":
        verify_password(username, password)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    # Generate a key only once (run this once to generate the key file)
    # Uncomment the next line if you haven't generated the key
    #generate_key()

    main()
