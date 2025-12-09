
import string
import math

COMMON = {"password", "123456", "qwerty", "letmein", "111111", "pass123"}

def score_password(pw: str) -> dict:
    score = 0
    notes = []

    
    if len(pw) >= 8:
        score += 1
    else:
        notes.append("short (<8)")
    if len(pw) >= 12:
        score += 1

   
    pools = 0
    if any(c.islower() for c in pw):
        pools += 26
        score += 1
    if any(c.isupper() for c in pw):
        pools += 26
        score += 1
    if any(c.isdigit() for c in pw):
        pools += 10
        score += 1
    if any(c in string.punctuation for c in pw):
        pools += len(string.punctuation)
        score += 1

    
    if pw.lower() in COMMON:
        notes.append("common password")
        score = max(score - 2, 0)

    
    pool = pools if pools > 0 else 1
    entropy = len(pw) * math.log2(pool)

    return {"password": pw, "score": score, "entropy": entropy, "notes": notes}

if __name__ == "__main__":
    tests = ["ThisIsMyPassword", "IloveMyC@t", "password", "CorrectHorseBatteryStaple","Danny123","Danny123!","Danny""123456","pass123"]
    for t in tests:
        print(score_password(t))
