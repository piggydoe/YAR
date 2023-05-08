import os
from cryptography.fernet import Fernet

# 5/8/22 - Encrypt files in directory - Written By Snowie

def rename_and_encrypt_files(directory):
    # Generate encryption key
    key = Fernet.generate_key()
    f = Fernet(key)

    # Iterate through files in directory
    for filename in os.listdir(directory):
        # Ignore subdirectories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Read file contents
        with open(os.path.join(directory, filename), 'rb') as file:
            data = file.read()

        # Encrypt file contents
        encrypted_data = f.encrypt(data)

        # Rename file with encrypted name
        encrypted_filename = f.encrypt(bytes(filename, 'utf-8'))
        os.rename(os.path.join(directory, filename), os.path.join(directory, encrypted_filename.decode('utf-8')))

        # Write encrypted data to file
        with open(os.path.join(directory, encrypted_filename.decode('utf-8')), 'wb') as file:
            file.write(encrypted_data)

    # Save encryption key to file
    with open(os.path.join(directory, 'key.key'), 'wb') as file:
        file.write(key)

rename_and_encrypt_files("D:\\Me\\code\\test\\TestEnc")