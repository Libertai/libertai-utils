from eth_account.messages import encode_defunct
from hexbytes import HexBytes
from web3 import Web3


def get_address_from_signature(message: str, signature: str) -> str:
    """Recover the Ethereum address used to sign the message"""
    w3 = Web3(Web3.HTTPProvider(""))
    encoded_message = encode_defunct(text=message)
    return w3.eth.account.recover_message(
        encoded_message,
        signature=HexBytes(signature),
    )


def format_eth_address(address: str) -> str:
    return address.lower()
