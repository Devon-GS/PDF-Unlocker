import os
import maskpass
from os import path
from PyPDF2 import PdfReader
from pypdf import PdfReader, PdfWriter



# Create folders
locked_files_folder = path.exists('locked_files')
processed_files = path.exists('processed_files')

if locked_files_folder == False:
    os.mkdir('locked_files')
if processed_files == False:
    os.mkdir('processed_files')

# Get list of files
file_list = os.listdir('locked_files')

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

# # Decrypt PDF
# for filename in file_list:
#     file = f'locked_files/{filename}'
#     output_path = 'processed_files/'
    
    
#     # Open files with reader
#     reader = PdfReader(file)
#     writer = PdfWriter()
    
#     # Check if encrypted
#     if reader.is_encrypted:
#         reader.decrypt(password)

#     # Add all pages to the writer
#     for page in reader.pages:
#         writer.add_page(page)

#    # Save decrypted file with new name in ouput folder
#     with open(f"{output_path}{new_file_name}.pdf", "wb") as f:
#         writer.write(f)