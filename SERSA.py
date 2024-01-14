import random

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair(p, q):
    """Generate a key pair (public key, private key)."""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose a random number e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    # Use extended Euclidean algorithm to find the modular inverse of e
    d = mod_inverse(e, phi)
    
    # Return the public key (n, e) and the private key (n, d)
    return (n, e), (n, d)

def gcd(a, b):
    """Calculate the greatest common divisor (gcd) of two numbers."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Calculate the modular inverse of a mod m using the extended Euclidean algorithm."""
    if gcd(a, m) != 1:
        raise ValueError("The modular inverse does not exist.")
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1,
            u2 - q * v2,
            u3 - q * v3,
            v1,
            v2,
            v3,
        )
    return u1 % m

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

# Example usage:
# Generate key pair
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

# Encrypt a message
#message = "Hello, RSA!"
message = input()
print("Original message: ",message)
encrypted_message = encrypt(public_key, message)
print("Encrypted message:", *encrypted_message)

# Decrypt the encrypted message
decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)
