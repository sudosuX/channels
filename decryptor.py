import pyzipper
import os

def unzip_password_protected_zip(zip_file_path, output_path, password):
    try:
        with pyzipper.AESZipFile(zip_file_path) as z:
            z.extractall(output_path, pwd=password.encode('utf-8'))
        print("Extraction successful.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_main_script():
    try:
        os.system("python main.py")
    except Exception as e:
        print(f"An error occurred while running main.py: {e}")

if __name__ == "__main__":
    zip_file_path = 'main.zip'  # Path to the encrypted ZIP file
    output_path = ''  # Path to extract the contents of the ZIP file
    password = os.environ.get("PASSWORD", "")  # Password obtained from environment variable

    unzip_password_protected_zip(zip_file_path, output_path, password)
    run_main_script()
