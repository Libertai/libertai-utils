from base64 import b32encode, b16decode

from typing_extensions import Literal


def get_vm_url(item_hash: str, url_type: Literal["host", "path"] = "host") -> str:
    if url_type == "path":
        return f"https://aleph.sh/vm/{item_hash}"

    # From aleph-client
    hash_base32 = b32encode(b16decode(item_hash.upper())).strip(b"=").lower().decode()
    return f"https://{hash_base32}.aleph.sh"