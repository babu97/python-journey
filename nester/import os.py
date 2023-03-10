import os
import shutil
import time

def rename_file(path):
    folder_name = os.path.basename(os.path.dirname(path))
    create_time = os.path.getctime(path)
    date_time = time.strftime("%Y%m%d-%H", time.gmtime(create_time))
    file_name = os.path.basename(path)
    new_name = f"{folder_name}_{date_time}"
    new_path = os.path.join(os.path.dirname(path), new_name)
    shutil.move(path, new_path)

# Example usage

folder_path = "G:\My Drive\kameme-unrefined"
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        rename_file(file_path)

