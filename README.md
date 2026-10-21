<h1 align="center">🔓 PDF Unlocker</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
  <!-- <img src="https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge" alt="Status"> -->
</p>

A stylish, automated command-line utility to batch decrypt and unlock PDF files. Drop your password-protected PDFs into a folder, type your password once, and let the script do the heavy lifting! 

Featuring secure, masked password inputs and an awesome ASCII art interface. 🎨

---

## ✨ Features

- **📂 Automatic Folder Management:** Automatically generates necessary directories (`locked_files` and `processed_files`) on the first run.
- **🗃️ Batch Processing:** Unlocks multiple PDF files simultaneously using a single password.
- **🔐 Secure Password Entry:** Uses `#` masking so your password is never visible on the screen.
- **🛡️ Error Handling:** Gracefully catches incorrect passwords, non-PDF files, and empty directories.

---

## 🛠️ Prerequisites

Before you begin, ensure you have **Python 3.x** installed on your system. 

You will also need to install the required third-party packages. You can install them via `pip`:

```bash
pip install poetry
```
```bash
poetry install
```

*(Note: Ensure your custom `error.py` file is located in the same directory as `main.py` for the custom exception handling to work).*

---

## 🚀 Getting Started

### 1. Clone or Download
Download the source code to your local machine and navigate to the directory:
```bash
cd path/to/pdf-unlocker
```

### 2. First Run (Setup)
Run the script for the first time to generate the required folders:
```bash
python main.py
```
*The script will create a `locked_files` and a `processed_files` directory, then pause.*

### 3. Add Your Files
Move or copy the encrypted PDF files you want to unlock into the newly created `locked_files` folder.

### 4. Unlock!
Press any key to continue (or run the script again). 
1. Enter the password for your locked PDFs.
2. Confirm the password.
3. The script will process the files and save the unlocked versions into the `processed_files` directory! 🎉

---

## 📁 Directory Structure

Once initialized, your project folder will look like this:

```text
📦 PDF-Unlocker
 ┣ 📂 locked_files/       <-- Place your password-protected PDFs here
 ┣ 📂 processed_files/    <-- Unlocked PDFs will be saved here
 ┣ 📜 main.py             <-- The main execution script
 ┗ 📜 error.py            <-- Custom error classes module
```

---

## ⚠️ Troubleshooting / Common Errors

| Error Message | Cause | Solution |
| :--- | :--- | :--- |
| **`FilesNotCreated`** | Folders didn't exist. | Normal behavior on first run. Add files to the created folders and press enter. |
| **`FolderIsEmpty`** | No PDFs found. | Place your locked PDFs into the `locked_files/` directory before continuing. |
| **`FileNotDecryptedError`** | Wrong Password. | Ensure you typed the correct password for the PDFs. |
| **`PdfStreamError`** | Invalid file type. | Ensure there are only `.pdf` files inside the `locked_files/` folder (no images, text files, etc). |

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).