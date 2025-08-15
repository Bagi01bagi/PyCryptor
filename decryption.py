import pyAesCrypt
import os
import sys

# function decryption
def decryption(file, password):
    # set the buffer size
    buffer_size = 512 * 1024

    # process only .crp files
    if not str(file).endswith(".crp"):
        return

    # output file without .crp extension
    out_file = str(os.path.splitext(file)[0])

    try:
        # call method of decryption
        pyAesCrypt.decryptFile(
            str(file),
            out_file,
            password,
            buffer_size
        )

        # to see result we will show decryption file
        print("[File '" + out_file + "' decrypted ]")

        # delete the original file using the remove method
        os.remove(file)

    except Exception as ex:
        print(f"[ERROR] {file} -> {ex}")
        # if the output file is empty or partially created, remove it
        if os.path.exists(out_file) and os.path.getsize(out_file) == 0:
            os.remove(out_file)

# scan function
def walking_by_dirs(dir, password):
    # Loop through all subdirectories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if we find the file, we decrypt it
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # if we find a directory, then we repeat the cycle in search of files
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль для расшифрования: ")
walking_by_dirs(r"C:\Users\Beauty\Desktop\mystaff", password)
# os.remove(str(sys.argv[0]))
