from pwdlib import PasswordHash

hashing = PasswordHash.recommended()

def create_hash_password(plain_password: str) -> str:
    return hashing.hash(plain_password)

def verify_hash_password(plain_password: str, hashed_password:str) -> bool:
    return hashing.verify(plain_password, hashed_password)