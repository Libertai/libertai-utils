from ecies.utils import generate_eth_key

from libertai_utils.utils.crypto import encrypt, decrypt


def test_encrypt():
    data = "Random secret data"

    eth_k = generate_eth_key()
    pk_hex = eth_k.public_key.to_hex()
    sk_hex = eth_k.to_hex()

    encrypted_data = encrypt(data, pk_hex)
    decrypted_data = decrypt(encrypted_data, sk_hex)
    assert decrypted_data == data
