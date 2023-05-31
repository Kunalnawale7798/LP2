def encrypt_transposition(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    num_rows = (len(plaintext) + key - 1) // key
    grid = [plaintext[i:i+key].ljust(key) for i in range(0, len(plaintext), key)]
    return ''.join(grid[col][row] for row in range(key) for col in range(num_rows))

def decrypt_transposition(ciphertext, key):
    num_cols = (len(ciphertext) + key - 1) // key
    grid = [ciphertext[i:i+num_cols] for i in range(0, len(ciphertext), num_cols)]
    return ''.join(grid[col][row] for row in range(num_cols) for col in range(key))

plaintext = "PVGCOE Nashik"
key = 5

ciphertext = encrypt_transposition(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_plaintext = decrypt_transposition(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)
