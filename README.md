# Password Security and Hashing Python Portfolio

This portfolio documents a set of Python scripts developed to explore password hashing, entropy measurement, and the use of salt and pepper for secure password storage.

---

## 1. Overview

The project contains three scripts designed to demonstrate secure password handling techniques:

1. **hasing_demo.py** – Demonstrates hashing passwords using MD5, SHA256, and bcrypt.
2. **password_meter.py** – Measures password strength based on length, character variety, and common password checks.
3. **salt_pepper_demo.py** – Shows the effects of adding salt and pepper to password hashing for improved security.

This suite is intended for educational purposes in cybersecurity, password management, and hashing techniques.

---

## 2. File Explanations

### 2.1 hasing_demo.py

**Purpose:** Demonstrates different hashing algorithms and verifies bcrypt hashes.

**Key Features:**

* Hashes user input with MD5, SHA256, and bcrypt.
* Shows how to verify a bcrypt hash.

**Usage:**

```
python hasing_demo.py
```

*(Insert screenshot showing user input, MD5, SHA256, and bcrypt outputs, including verification)*

---

### 2.2 password_meter.py

**Purpose:** Evaluate the strength of passwords and calculate entropy.

**Key Features:**

* Scores passwords based on length, character diversity, and common password checks.
* Calculates estimated entropy of the password.
* Provides notes on weaknesses.

**Usage:**

```
python password_meter.py
```

*(Insert screenshot showing password strength scores, entropy values, and notes for a series of test passwords)*

---

### 2.3 salt_pepper_demo.py

**Purpose:** Demonstrate the security benefits of adding salt and pepper to password hashes.

**Key Features:**

* Shows that identical passwords produce identical hashes without salt.
* Uses random salt to produce different hashes for the same password.
* Combines salt and pepper to further improve security.

**Usage:**

```
python salt_pepper_demo.py
```

*(Insert screenshot showing outputs for unsalted, salted, and salted+peppered hashes, highlighting the differences)*

---

## 3. Workflow Demonstration

1. **Hashing Demo:** Run `hasing_demo.py` to observe basic hashing and verification techniques.
2. **Password Strength:** Run `password_meter.py` to assess and score password strength.
3. **Salt and Pepper:** Run `salt_pepper_demo.py` to understand the effects of salt and pepper on hash uniqueness.

*(Insert a series of screenshots showing the workflow from hashing to strength measurement to salt and pepper demonstration.)*

---

## 4. Conclusion

This collection of scripts provides a practical introduction to password security:

* Hashing with MD5, SHA256, and bcrypt.
* Evaluating password strength and entropy.
* Enhancing password security using salt and pepper.

It is suitable for:

* Learning secure password storage techniques.
* Understanding the differences between hash algorithms.
* Exploring methods to prevent hash collisions and dictionary attacks.

---

*(Add all relevant screenshots where indicated to complete the portfolio.)*
