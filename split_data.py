import os
import shutil
import random


BASE_DIR = os.getcwd()
CHAR_DIR = os.path.join(BASE_DIR, 'Char')

TRAIN_DIR = os.path.join(BASE_DIR, 'train')
VALID_DIR = os.path.join(BASE_DIR, 'valid')
TEST_DIR = os.path.join(BASE_DIR, 'test')


os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(VALID_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)

counter = 0
for char in os.listdir(CHAR_DIR):
    char_folder = os.path.join(CHAR_DIR, char)
    if os.path.isdir(char_folder):
        files = os.listdir(char_folder)
        random.shuffle(files)
        
        if len(files) < 40:
            print(f"Not enough images for character {char}")
            continue

        train_files = files[:40]
        valid_files = files[40:45]
        test_files = files[45:]

        train_char_dir = os.path.join(TRAIN_DIR, char)
        valid_char_dir = os.path.join(VALID_DIR, char)
        test_char_dir = os.path.join(TEST_DIR, char)
        
        os.makedirs(train_char_dir, exist_ok=True)
        os.makedirs(valid_char_dir, exist_ok=True)
        os.makedirs(test_char_dir, exist_ok=True)

        for file in train_files:
            shutil.copy(os.path.join(char_folder, file), os.path.join(train_char_dir, file))
        for file in valid_files:
            shutil.copy(os.path.join(char_folder, file), os.path.join(valid_char_dir, file))
        for file in test_files:
            shutil.copy(os.path.join(char_folder, file), os.path.join(test_char_dir, file))

        print(f"Processed character {char}: {len(train_files)} train, {len(valid_files)} valid,{len(test_files)} test")
    counter = counter + 1
    if counter == 100:
        break


print("Splitting complete.")
