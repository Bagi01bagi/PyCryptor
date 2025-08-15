import pyAesCrypt
import os

# function encryption
def encryption(file, password):
    # set the buffer size
    buffer_size = 512 * 1024

    # skip already-encrypted files
    if str(file).endswith(".crp"):
        return

    # call method of encryption
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # show result
    print("[File '" + os.path.basename(str(os.path.splitext(file)[0])) + "' encrypted]")

    # delete the original file (be careful!)
    #os.remove(file)

# scan function
def walking_by_dirs(directory, password):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Folder not found: {directory}")

    # Loop through all subdirectories in the specified directory
    for name in os.listdir(directory):
        path = os.path.join(directory, name)

        # optionally skip common service folders
        if os.path.basename(path) in {'.git', '.venv', '__pycache__'}:
            continue

        # if we find a file, we encrypt it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print("[SKIP]", path, "->", ex)
        # if we find a directory, then we repeat the cycle in search of files
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль для шифрования: ").strip()
# use raw string to avoid backslash escapes on Windows
walking_by_dirs(r"C:\Users\Beauty\Desktop\mystaff", password)
# os.remove(str(sys.argv[0]))
