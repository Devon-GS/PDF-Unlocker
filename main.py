import os
import maskpass
from art import *
from os import path
import error as e
from PyPDF2 import PdfReader
from pypdf import PdfReader, PdfWriter
from pypdf.errors import FileNotDecryptedError, PdfStreamError

#############################################################################
# ASCII ART
#############################################################################
tprint('PDF UNLOCKER')

#############################################################################
# CHECK FOLDERS ARE CREATED
#############################################################################
try:
    locked_files_folder = path.exists('locked_files')
    processed_files = path.exists('processed_files')

    if locked_files_folder == False or processed_files == False:
        raise e.FilesNotCreated 
    
except e.FilesNotCreated:
        os.mkdir('locked_files')
        os.mkdir('processed_files')
        input('Files created! Please copy PDF files into locked_files and press any button to continue: ')
        print('################################################################################')

#############################################################################
# CHECK ENTERED PASSWORD IS CORRECT
#############################################################################

match = 0

while match == 0:
    password = maskpass.askpass(prompt="Please Type Password: ", mask="#") 
    password2 = maskpass.askpass(prompt="Please Retype Password: ", mask="#")

    if password == password2:
        match = 1
    else:
        print("Password do not match, Please type them again") 


#############################################################################
# DECRYPT PDF FILES AND RENAME THEM
#############################################################################

try:
    # Get list of files
    file_list = os.listdir('locked_files')
    if not file_list:
        raise e.FolderIsEmpty

    # Decrypt PDF
    for filename in file_list:
        file = f'locked_files/{filename}'
        output_path = 'processed_files/'
        
        # Open files with reader
        reader = PdfReader(file)
        writer = PdfWriter()
        
        # Check if encrypted
        if reader.is_encrypted:
            reader.decrypt(password)

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

    # Save decrypted file with new name in ouput folder
        with open(f"{output_path}{filename}.pdf", "wb") as f:
            writer.write(f)

except FileNotDecryptedError:
    print('################################################################################')
    print('The files was not decrypted! Please make sure you used the correct password')

except PdfStreamError:
    print('################################################################################')
    print('There was an error decrypting your files! Please check locked_files folder for non PDF files')

except e.FolderIsEmpty:
    print('################################################################################')
    print('locked_file folder is empty!')

