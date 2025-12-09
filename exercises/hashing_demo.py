
import hashlib
import bcrypt

def md5_hash(pw: str) -> str:
    return hashlib.md5(pw.encode()).hexdigest()

def sha256_hash(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

def bcrypt_hash(pw: str, rounds: int = 12) -> bytes:
    salt = bcrypt.gensalt(rounds)
    return bcrypt.hashpw(pw.encode(), salt)

def bcrypt_check(pw: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(pw.encode(), hashed)

if __name__ == "__main__":
    pw = input("Enter a password to hash: ")

    print("\n--- HASH OUTPUTS ---")
    print("MD5    :", md5_hash(pw))
    print("SHA256 :", sha256_hash(pw))

    b = bcrypt_hash(pw)
    print("bcrypt :", b)
    print("Verify bcrypt:", bcrypt_check(pw, b))
