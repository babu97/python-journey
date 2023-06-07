# import os
# import shutil
# import datetime
# import time
from mattermostdriver import Driver

# Initialize Mattermost driver with your bot token and server URL
driver = Driver({
    'url': 'rosetta.cloud.mattermost.com',
    'token': 'jpfycxsah7f75msoig34zafwhh',
    'scheme': 'https',
    'port': 443
 
})

# # Specify the Mattermost channel to send notifications to

# # Specify the root directory where the folders are located
# root_directory = 'G:\My Drive\Media Monitoring'

# # Loop through each folder in the root directory
# for folder_name in os.listdir(root_directory):
#     # Get the full path of the folder
#     folder_path = os.path.join(root_directory, folder_name)
#     # Check if the path is a directory
#     if os.path.isdir(folder_path):
#         # Loop through each file in the folder
#         for file_name in os.listdir(folder_path):
#             # Get the full path of the file
#             file_path = os.path.join(folder_path, file_name)
#             # Check if the path is a file
#             if os.path.isfile(file_path):
#                 try:
#                     # Check file size and skip if less than 10MB
#                     file_size = os.path.getsize(file_path)
#                     if file_size < 10 * 1024 * 1024:
#                         print(f'Skipping file {file_name} in folder {folder_name}: file size is less than 10MB.')
#                         continue

#                     # Get the creation time of the file
#                     created = os.path.getctime(file_path)
#                     time_diff = time.time() - created
#                     # Check if the file was created more than 1 hour ago
#                     if time_diff >= 3600:
#                         # Convert the creation time to a datetime object
#                         created_datetime = datetime.datetime.fromtimestamp(created)
#                         # Get the year, month, and day of creation
#                         year = str(created_datetime.year)
#                         month = str(created_datetime.month).zfill(2)
#                         day = str(created_datetime.day).zfill(2)
#                         hour = str(created_datetime.hour).zfill(2)
#                         # Generate the new filename with the hour of creation
#                         new_file_name = f'{year}-{month}-{day}_{hour}'
#                         # Check if the new filename already exists in the folder
#                         while os.path.exists(os.path.join(folder_path, new_file_name)):
#                             # If the new filename already exists, add "-1" to the end of the filename and check again
#                             new_file_name = f'{year}-{month}-{day}_{hour}-1'
#                             hour = str(int(hour) + 1).zfill(2)
#                             new_file_name = f'{year}-{month}-{day}_{hour}'

#                         # Rename the file with the new filename
#                         os.rename(file_path, os.path.join(folder_path, new_file_name))

#                         # Wait for renaming to complete before moving the file
#                         while not os.path.exists(os.path.join(folder_path, new_file_name)):
#                             time.sleep(0.3)

#                         # Create subfolders according to year, month, and day
#                         year_folder = os.path.join(folder_path, year)
#                         month_folder = os.path.join(year_folder, month)
#                         day_folder = os.path.join(month_folder, day)
#                         for folder in [year_folder, month_folder, day_folder]:
#                             if not os.path.exists(folder):
#                                 os.mkdir(folder)

#                         # Move the file to the day subfolder
#                         shutil.move(os.path.join(folder_path, new_file_name), os.path.join(day_folder, new_file_name))

# Send Mattermost notification to channel when renaming and uploading is done
driver.login()
channel_id = 'b6xrg4zw4pggjk4ngkoseuau6r'
message = 'testing from api'
driver.posts.create_post({
    'channel_id': channel_id,
    'message': message

})
driver.logout()
