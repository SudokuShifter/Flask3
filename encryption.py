from cryptography.fernet import Fernet


KEY = Fernet.generate_key()
CIPHER_SUITE = Fernet(KEY)


def encryption_pass(password: str):
    return CIPHER_SUITE.encrypt(password.encode('UTF-8')).decode()


def decryption_pass(encrypt_pass: str):
    return CIPHER_SUITE.decrypt(encrypt_pass.encode('UTF-8')).decode()
