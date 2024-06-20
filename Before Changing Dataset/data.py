import os
import shutil
from collections import Counter

BASE_DIR = os.getcwd()
CHAR_DIR = os.path.join(BASE_DIR, 'Char')

FIRST_DIR = os.path.join(BASE_DIR, '1', 'cleaned_data(50_50)')
SECOND_DIR = os.path.join(BASE_DIR, '2', 'cleaned_data(50_50)')
THIRD_DIR = os.path.join(BASE_DIR, '3', 'cleaned_data(50_50)')
FORTH_DIR = os.path.join(BASE_DIR, '4', 'cleaned_data(50_50)')

directories = [FIRST_DIR, SECOND_DIR, THIRD_DIR, FORTH_DIR]

char_counter = Counter()

char_class = os.listdir(CHAR_DIR)


file_txt = open('char.txt','w',encoding='utf-8')

for item in char_class:
    file_txt.write(item+'\n')


for directory in directories:
    if os.path.exists(directory):
        files = os.listdir(directory)
        
        for file in files:
            char = file.split('_')[0]
            char_counter[char] += 1
    else:
        print(f"The directory {directory} does not exist.")

if not os.path.exists(CHAR_DIR):
    os.makedirs(CHAR_DIR)

for directory in directories:
    if os.path.exists(directory):
        files = os.listdir(directory)
        for file in files:
            char = file.split('_')[0]
            char_folder = os.path.join(CHAR_DIR, char)
            if not os.path.exists(char_folder):
                os.makedirs(char_folder)
            source_path = os.path.join(directory, file)
            destination_path = os.path.join(char_folder, file)
            shutil.copy(source_path, destination_path)
            print(f"Copied {file} to {char_folder}")
    else:
        print(f"The directory {directory} does not exist.")

print("All files have been copied to their respective character folders.")
