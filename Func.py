def encrypt(public_key, message):
    """Encrypt a message using the public key."""
    n, e = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg

def decrypt(private_key, encrypted_message):
    """Decrypt an encrypted message using the private key."""
    n, d = private_key
    decrypted_msg = [chr(pow(char, d, n)) for char in encrypted_message]
    return "".join(decrypted_msg)
