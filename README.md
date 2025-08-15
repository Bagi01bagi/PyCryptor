# 🔐 AES-256 File Encryption & Decryption Tool

🔒💾 Lightweight Python script for AES-256 file encryption & decryption with 📂 folder recursion and safe `.crp` handling.

---

## 📌 Features
- AES-256 encryption using [`pyAesCrypt`](https://pypi.org/project/pyAesCrypt/)
- Encrypt or decrypt all files in a folder (including subfolders)
- Processes only `.crp` files during decryption to prevent errors
- Optional deletion of original files after processing
- Simple command-line interface

---

## 🛠 Requirements
- Python 3.x  
- Install dependencies:
```bash
pip install pyAesCrypt
