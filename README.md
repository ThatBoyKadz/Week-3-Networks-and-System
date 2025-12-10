<b>Cybersecurity & Password Management Exercises<b>


this Project showcases practical exercises completed during the course on cybersecurity fundamentals, focusing on password security. 
The exercises include:

Hashing passwords using different algorithms
Evaluating password strength using scoring and entropy
Demonstrating the effect of salt and pepper on password hashing
Each exercise includes code samples, explanations, and outputs demonstrating the concepts learned.

<b>Hashing Passwords: hashing_demo.py<b> 

<img width="423" height="127" alt="image" src="https://github.com/user-attachments/assets/4b084ed6-b67d-4204-aea1-2ed055ba9044" />
<img width="420" height="65" alt="image" src="https://github.com/user-attachments/assets/86c0294f-f949-4399-8117-e30e6f4b3635" />
Explanation:

--MD5 and SHA256 provide basic hashing.
--bcrypt includes a salt by default and supports secure verification.
--Demonstrates secure password storage practices.



Outcome: 
<img width="457" height="101" alt="image" src="https://github.com/user-attachments/assets/eefbb815-416d-48fc-9449-8d35614f2afa" />


<b>Password Strength Meter: password_meter.py<b>

The objective of this code is to evaluate password strength based on length, character diversity, and entropy.

<img width="387" height="265" alt="image" src="https://github.com/user-attachments/assets/bceaea64-7363-4818-b25e-391f88684dec" />

This code is the character pools, it counts how many types of characters the password contains: lowercase letters - 26 , uppercase letters - 26 , digits - 10. This adds protection because represents the number of unique characters an attacker might have to guess.



<b>salt_pepper_demo.py : salt + pepper hashing<b>


<img width="521" height="146" alt="image" src="https://github.com/user-attachments/assets/8c9978c9-e49f-4da2-9e0b-5bf54d60ffce" />


Pepper - a secrect fixed value added to the password to make it harder for attackers to crack hashes. Pepper is stored securely in code or an environment variable

Hash_with_salt_and_pepper; "os.urandom(16)" generates a 16-byte random salt, the password is combined with the salt and pepper: salt + pepper.encode() + pepper. 
using both salt and pepper greatly increases security, salt ensures each hash is unique, and pepper adds an extra secret layer, protecting against hash leaks.
