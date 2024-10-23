import json
import os
import random
import string
from datetime import datetime
from PIL import Image
import glob

def print_to_txt(value, filename="output", dir="logs", sequential=False):
    current_time = datetime.now()
    ms = current_time.strftime("%H%M%S") + f".{current_time.microsecond // 1000:03}.{current_time.microsecond % 1000:03}"
    if sequential: 
        filename = f'{filename}-{ms}'
    with open(f'{dir}/{filename}.txt', 'w') as file:
        if isinstance(value, (list, dict, tuple)):
            file.write(json.dumps(value))
        else:
            file.write(str(value))
    
    print(f"Value has been written to {filename}.txt")

def clear_txt_files(dir="logs"):
    txt_files = glob.glob(os.path.join(dir, "*.txt"))
    for file in txt_files:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Error deleting {file}: {e}")
    print(f"Cleared {len(txt_files)} .txt files in the directory: {dir}")