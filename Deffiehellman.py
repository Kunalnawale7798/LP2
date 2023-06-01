import random

def generate_private_key(p):
    # Generate a private key in the range [2, p-2]
    return random.randint(2, p-2)

def generate_public_key(g, private_key, p):
    # Calculate the public key as g^private_key mod p
    return pow(g, private_key, p)

def generate_shared_secret(public_key, private_key, p):
    # Calculate the shared secret as public_key^private_key mod p
    return pow(public_key, private_key, p)

# Common parameters
p = 23  # Prime number
g = 5   # Primitive root

# Alice's key generation
alice_private_key = generate_private_key(p)
alice_public_key = generate_public_key(g, alice_private_key, p)

# Bob's key generation
bob_private_key = generate_private_key(p)
bob_public_key = generate_public_key(g, bob_private_key, p)

# Shared secret calculation
alice_shared_secret = generate_shared_secret(bob_public_key, alice_private_key, p)
bob_shared_secret = generate_shared_secret(alice_public_key, bob_private_key, p)

# Verify shared secrets match
assert alice_shared_secret == bob_shared_secret

# Print the shared secret
print("Shared Secret:", alice_shared_secret)
