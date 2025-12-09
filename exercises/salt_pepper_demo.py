import hashlib
import os


password = "user123password"

hash1 = hashlib.sha256(password.encode()).hexdigest()
hash2 = hashlib.sha256(password.encode()).hexdigest()

print("Without Salt:")
print("Hash 1:", hash1)
print("Hash 2:", hash2)
print("Hashes are identical:", hash1 == hash2)
print("-" * 50)


def hash_with_salt(password):
    salt = os.urandom(16)
    salted_password = salt + password.encode()
    hashed = hashlib.sha256(salted_password).hexdigest()
    return hashed, salt

hash_salt1, salt1 = hash_with_salt(password)
hash_salt2, salt2 = hash_with_salt(password)

print("With Salt:")
print("Hash 1:", hash_salt1)
print("Hash 2:", hash_salt2)
print("Hashes are identical:", hash_salt1 == hash_salt2)
print("-" * 50)


PEPPER = b"MySecretPepper123!"  

def hash_with_salt_and_pepper(password):
    salt = os.urandom(16)
    salted_peppered_password = salt + password.encode() + PEPPER
    hashed = hashlib.sha256(salted_peppered_password).hexdigest()
    return hashed, salt

hash_sp1, sp_salt1 = hash_with_salt_and_pepper(password)
hash_sp2, sp_salt2 = hash_with_salt_and_pepper(password)

print("With Salt + Pepper:")
print("Hash 1:", hash_sp1)
print("Hash 2:", hash_sp2)
print("Hashes are identical:", hash_sp1 == hash_sp2)
