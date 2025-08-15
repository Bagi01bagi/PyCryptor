import pyAesCrypt
import os

# function decryption
def decryption(file, password):
    # set the buffer size
    buffer_size = 512 * 1024

    # process only .crp files
    if not str(file).endswith(".crp"):
        return

    out_file = str(os.path.splitext(file)[0])

    try:
        # call method of decryption
        pyAesCrypt.decryptFile(
            str(file),
            out_file,
            password,
            buffer_size
        )

        # show result
        print("[File '" + out_file + "' decrypted]")

        # delete the original encrypted file
        #os.remove(file)

    except Exception as ex:
        print("[ERROR]", file, "->", ex)
        # if output file was created but empty (failed), remove it
        if os.path.exists(out_file) and os.path.getsize(out_file) == 0:
            os.remove(out_file)

# scan function
def walking_by_dirs(directory, password):
    # Loop through all subdirectories in the specified directory
    for name in os.listdir(directory):
        path = os.path.join(directory, name)

        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль для расшифрования: ").strip()
# use raw string to avoid backslash issues; Desktop с заглавной буквы
walking_by_dirs(r"C:\Users\Beauty\Desktop\mystaff", password)
# os.remove(str(sys.argv[0]))
