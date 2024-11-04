from libertai_utils.chains.ethereum import is_eth_signature_valid, format_eth_address
from libertai_utils.chains.solana import is_solana_signature_valid
from libertai_utils.interfaces.subscription import SubscriptionChain


def is_signature_valid(chain: SubscriptionChain, message: str, signature: str, address: str) -> bool:
    valid = False

    if chain == SubscriptionChain.base:
        valid = is_eth_signature_valid(message, signature, address)
    elif chain == SubscriptionChain.solana:
        valid = is_solana_signature_valid(message, signature, address)

    return valid


def format_address(address: str, chain: SubscriptionChain) -> str:
    if chain == SubscriptionChain.base:
        return format_eth_address(address)
    return address
