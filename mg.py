import os
import shutil
import datetime

# Specify the root directory where the folders are located
root_directory = "G:\My Drive\KAMEMEME VM"

# Loop through each folder in the root directory
for folder_name in os.listdir(root_directory):
    # Get the full path of the folder
    folder_path = os.path.join(root_directory, folder_name)
    # Check if the path is a directory
    if os.path.isdir(folder_path):
        # Loop through each file in the folder
        for file_name in os.listdir(folder_path):
            # Get the full path of the file
            file_path = os.path.join(folder_path, file_name)
            # Check if the path is a file
            if os.path.isfile(file_path):
                # Get the creation time of the file
                created = os.path.getctime(file_path)
                # Convert the creation time to a datetime object
                created_datetime = datetime.datetime.fromtimestamp(created)
                # Get the year, month, and day of creation
                year = str(created_datetime.year)
                month = str(created_datetime.month).zfill(2)
                day = str(created_datetime.day).zfill(2)
                hour = str(created_datetime.hour).zfill(2)
                # Rename the file with the hour of creation
                new_file_name = "{}_{}".format(hour, file_name)
                os.rename(file_path, os.path.join(folder_path, new_file_name))
                # Create subfolders according to year, month, and day
                year_folder = os.path.join(folder_path, year)
                month_folder = os.path.join(year_folder, month)
                day_folder = os.path.join(month_folder, day)
                for folder in [year_folder, month_folder, day_folder]:
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                # Move the file to the day subfolder
                shutil.move(os.path.join(folder_path, new_file_name), os.path.join(day_folder, new_file_name))
