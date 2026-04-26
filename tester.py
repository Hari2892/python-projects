# This script demonstrates how to generate a SHA-1 hash from a given string using Python's built-in hashlib library.

import hashlib

def generate_sha1_hash(text):
    # 1. Encode the string to bytes
    encoded_text = text.encode('utf-8')
    
    # 2. Create a SHA-1 hash object
    sha1_hash = hashlib.sha1(encoded_text)
    
    # 3. Get the hexadecimal representation of the hash
    hex_digest = sha1_hash.hexdigest()
    
    return hex_digest

# Example usage:
my_string = "123456789"
hashed_string = generate_sha1_hash(my_string)

print(f"Original String: {my_string}")
print(f"SHA-1 Hash:      {hashed_string}")