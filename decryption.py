import pyAesCrypt
import os 
import sys


#function dencryption
def decryption(file,password):
    #set the buffer size
    buffer_size = 512 * 1024

    # call method of decryption
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    #to see result we will show encryption file
    print("[File '" + str(os.path.splitext(file)[0])+ "' decrypted ]")

    # delete the original file using the remove method
    os.remove(file)
#scan function
def walking_by_dirs(dir, password):
    #Loop through all subdirectories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if we find the file, we decrypt it 
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        #if we find a directory, then we repeat the cycle in search of files        
        else:
            walking_by_dirs(path, password)  
password= input("Ввидите пароль для разшифрования: ")    
walking_by_dirs(r"C:\Users\Beauty\desktop\mystaff", password)
#os.remove(str(sys.argv[0]))
