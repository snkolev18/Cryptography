from cryptography.fernet import Fernet #used for the encryption of the data

if __name__ == "__main__":
    pub_key = Fernet.generate_key()
    print(pub_key)