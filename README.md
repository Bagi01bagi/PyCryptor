# 🔐 AES-256 File Encryption & Decryption Tool

🔒💾 Lightweight Python script for AES-256 file encryption & decryption with 📂 folder recursion and safe `.crp` handling.

---

## 📌 Features
- AES-256 encryption using [`pyAesCrypt`](https://pypi.org/project/pyAesCrypt/)
- Encrypt or decrypt all files in a folder (including subfolders)
- Simple command-line interface
- Optional deletion of original files after processing

---

## 🛠 Requirements
- Python 3.x  
- Install dependencies:
```bash
pip install pyAesCrypt
```


```bash python encryptions.py```
## The script will:

Ask for a password.

Encrypt all files in the specified folder.

Save them with a .crp extension.

Delete the original files (optional).

```bash python decryptions.py```

## The script will:

Ask for a password.

Decrypt all .crp files in the folder.

Restore them to their original names.

Delete the encrypted files after successful decryption.
