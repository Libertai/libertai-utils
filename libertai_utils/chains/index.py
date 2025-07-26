from libertai_utils.chains.ethereum import (
    is_eth_signature_valid,
    format_eth_address,
    is_eth_address,
)
from libertai_utils.chains.solana import is_solana_signature_valid, is_solana_address
from libertai_utils.interfaces.blockchain import LibertaiChain


def is_signature_valid(
    chain: LibertaiChain, message: str, signature: str, address: str
) -> bool:
    valid = False

    if chain == LibertaiChain.base:
        valid = is_eth_signature_valid(message, signature, address)
    elif chain == LibertaiChain.solana:
        valid = is_solana_signature_valid(message, signature, address)

    return valid


def is_address_valid(chain: LibertaiChain, address: str) -> bool:
    if chain == LibertaiChain.base:
        return is_eth_address(address)
    elif chain == LibertaiChain.solana:
        return is_solana_address(address)

    return False


def format_address(chain: LibertaiChain, address: str) -> str:
    if chain == LibertaiChain.base:
        return format_eth_address(address)
    elif chain == LibertaiChain.solana:
        return address  # Solana addresses are already in base58 format
    return address
