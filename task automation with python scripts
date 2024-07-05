import os
import shutil

# Define the directory to organize
directory_to_organize = "path_to_your_directory"  # Replace with your directory path

# Define a mapping of file extensions to directory names
file_type_directories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Scripts': ['.py', '.sh', '.bat']
}

# Create directories if they don't exist
for directory in file_type_directories.keys():
    dir_path = os.path.join(directory_to_organize, directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Function to get the directory name based on file extension
def get_directory_for_extension(extension):
    for directory, extensions in file_type_directories.items():
        if extension.lower() in extensions:
            return directory
    return 'Others'

# Create 'Others' directory for uncategorized files
others_directory = os.path.join(directory_to_organize, 'Others')
if not os.path.exists(others_directory):
    os.makedirs(others_directory)

# Organize files
for filename in os.listdir(directory_to_organize):
    file_path = os.path.join(directory_to_organize, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1]
        target_directory = get_directory_for_extension(file_extension)
        target_path = os.path.join(directory_to_organize, target_directory, filename)
        shutil.move(file_path, target_path)
        print(f"Moved: {filename} to {target_directory}")

print("File organization complete.")
