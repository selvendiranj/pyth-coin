import hashlib
import json


def hash(block):
    """
    Creates a SHA-256 hash of a Block

    :param block: Block
    """

    # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()


def get_proof_of_work(last_block):
    """
    Simple Proof of Work Algorithm:

        - Find a number p' such that hash(pp') contains leading 4 zeroes
        - Where p is the previous proof, and p' is the new proof

    :param last_block: <dict> last Block
    :return: <int>
    """

    last_proof = last_block['proof']
    last_hash = hash(last_block)

    proof = 0
    while is_proof_valid(last_proof, proof, last_hash) is False:
        proof += 1

    return proof


def is_proof_valid(last_proof, proof, last_hash):
    """
    Validates the Proof

    :param last_proof: <int> Previous Proof
    :param proof: <int> Current Proof
    :param last_hash: <str> The hash of the Previous Block
    :return: <bool> True if correct, False if not.

    """

    guess = f'{last_proof}{proof}{last_hash}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    """print('\n')
    print('last_proof:', last_proof)
    print('proof:', proof)
    print('last_hash:', last_hash)
    print('guess:', f'{last_proof}{proof}{last_hash}')
    print('encoded_guess:', guess)
    print('hashed_guess:', guess_hash)"""

    return guess_hash[:4] == "0000"


lastBlock = {
    "index": 1,
    "timestamp": 1506057125.900785,
    "transactions": [{
        "sender": "8527147fe1f5426f9dd545de4b27ee00",
        "recipient": "a77f5cdfa2934df3954a5c7c7da5df1f",
        "amount": 5
    }],
    "proof": 324984774000,
    "previous_hash": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}

proof = get_proof_of_work(lastBlock)
print('proof:', proof)
