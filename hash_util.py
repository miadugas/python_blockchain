import hashlib as hl
import json

def hash_string_256(string):
    """Create a SHA256 hash for a given input string.

    Arguments:
        :string: The string which should be hashed.
    """
    return h1.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it.
    
    Arguments:
        :block: The block that should be hashed.
    """
    """Modify the hash for security with hashlib & json """
    return hash_string_256(json.dumps(block, sort_keys=True).encode())