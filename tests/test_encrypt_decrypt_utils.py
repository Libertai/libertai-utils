from ecies.utils import generate_eth_key
from libertai.crypto.common import decrypt_secret, encrypt_secret


def test_encrypt():
    my_secret = "my secret".encode()
    eth_k = generate_eth_key()
    pk_hex = eth_k.public_key.to_hex()
    encrypted_secret = encrypt_secret(pk_hex, my_secret)
    assert isinstance(encrypted_secret, bytes)

    sk_hex = eth_k.to_hex()
    decrypted_secret = decrypt_secret(sk_hex, encrypted_secret)
    assert isinstance(encrypted_secret, bytes)
    assert decrypted_secret == my_secret
