import os
from cryptography.fernet import Fernet

# 5/8/23 - Decrypt files in a directory using a key file - Written by Snowie

def decrypt_files(directory, key_filepath):
    # Load encryption key from file
    with open(key_filepath, 'rb') as file:
        key = file.read()
    f = Fernet(key)

    # Iterate through files in directory
    for encrypted_filename in os.listdir(directory):
        # Ignore subdirectories and key file
        if os.path.isdir(os.path.join(directory, encrypted_filename)) or encrypted_filename == "key.key":
            continue

        # Decrypt file contents
        with open(os.path.join(directory, encrypted_filename), 'rb') as file:
            encrypted_data = file.read()
        data = f.decrypt(encrypted_data)

        # Rename file with decrypted name
        decrypted_filename = f.decrypt(bytes(encrypted_filename, 'utf-8'))
        os.rename(os.path.join(directory, encrypted_filename), os.path.join(directory, decrypted_filename.decode('utf-8')))

        # Write decrypted data to file
        with open(os.path.join(directory, decrypted_filename.decode('utf-8')), 'wb') as file:
            file.write(data)

decrypt_files("D:\\Me\\code\\test\\Test", "D:\\Me\\code\\test\\Test" + "\\key.key")