import pyAesCrypt
import os 
import sys 

# enable deletion of originals after encryption (CAUTION!)
DELETE_ORIGINALS = False
#function encryption
def encryption(file,password):
    #set the buffer size
    buffer_size = 512 * 1024
    
    # skip already encrypted files
    if str(file).endswith(".crp"):
        return
    # call method of encryption
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    #to see result we will show encryption file
    print("[File '" + str(os.path.splitext(file)[0])+ "' encrypted ]")

    #  delete the original file if necessary
    if DELETE_ORIGINALS:
        os.remove(file)
    
#scan function
def walking_by_dirs(dir, password):
    #Loop through all subdirectories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if we find the file, we decrypt it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        #if we find a directory, then we repeat the cycle in search of files       
        else:
            walking_by_dirs(path, password)  
password= input("Ввидите пароль для шифрования: ")    
walking_by_dirs(r"C:\Users\Beauty\desktop\mystaff", password) 
#os.remove(str(sys.argv[0]))  
#                   