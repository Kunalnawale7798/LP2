from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return base64.b64encode(ciphertext).decode('utf-8')

def aes_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')

# Example usage
key = get_random_bytes(16)  # 16 bytes key for AES-128
plaintext = "This is a secret message"

encrypted = aes_encrypt(key, plaintext)
print("Encrypted ciphertext:", encrypted)

decrypted = aes_decrypt(key, encrypted)
print("Decrypted plaintext:", decrypted)
