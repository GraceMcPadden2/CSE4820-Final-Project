import os
import shutil
 
source_dir =  "/Users/grace/Desktop/Data/Original" #Replace with path to data on device
jpg_dir = "/Users/grace/Desktop/Weapons/jpg"
txt_dir = "/Users/grace/Desktop/Weapons/txt"


for file in os.listdir(source_dir):
    full_path = os.path.join(source_dir, file)
    if file.lower().endswith("jpg"):
        shutil.move(full_path, os.path.join(jpg_dir, file))
        print(f"Moved JPG: {file}")

    if file.lower().endswith("txt"):
        shutil.move(full_path, os.path.join(txt_dir, file))
        print(f"Moved TXT: {file}")

#reverse
# for file in os.listdir(jpg_dir):
#     full_path = os.path.join(jpg_dir, file)
#     shutil.move(full_path, os.path.join(source_dir, file))
