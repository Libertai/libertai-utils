import base64

from ecies import encrypt as ecies_encrypt, decrypt as ecies_decrypt


def encrypt(data: str, public_key: str | bytes) -> str:
    """Encrypt some data with a public key"""

    encrypted_data = ecies_encrypt(public_key, data.encode())
    # Encoding it in base64 to avoid data loss when stored on Aleph
    base64_encrypted_data = base64.b64encode(encrypted_data).decode()

    return base64_encrypted_data


def decrypt(data: str, private_key: str | bytes) -> str:
    """Decrypt data with a private key"""

    # Decode the base64 data
    encrypted_data = base64.b64decode(data)
    decrypted_data = ecies_decrypt(private_key, encrypted_data).decode()

    return decrypted_data
