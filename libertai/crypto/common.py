from uuid import uuid4

from ecies import decrypt, encrypt


def generate_unique_token() -> str:
    return uuid4().hex


def encrypt_secret(pk_hex: hex, secret: bytes) -> bytes:
    return encrypt(pk_hex, secret)


def decrypt_secret(sk_hex: str, encrypted_secret: bytes) -> bytes:
    return decrypt(sk_hex, encrypted_secret)
