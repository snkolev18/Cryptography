from cryptography.fernet import Fernet #used for the encryption of the data

if __name__ == "__main__":
    priv_key = Fernet.generate_key()
    print(priv_key)

    message = "Imam 200k leva vkushti i parolata za seifa e 1234"
    msg_bin = message.encode()

    enc = Fernet(priv_key)

    enc_msg = enc.encrypt(msg_bin) #encrypting the message
    print(enc_msg)

    dec_msg = enc.decrypt(enc_msg) #decrypting the message
    print(dec_msg)