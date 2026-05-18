#Automatically move files from your Downloads folder into categorized subfolders (e.g., PDFs → Documents, Images → Pictures, etc.).
import os
import shutil

# Define source (Downloads) and destination folders
source_folder = r"C:\Users\DELL\Downloads"
destination_folder = r"C:\Users\DELL\Downloads\Organized"

# File type categories
file_types = {
      "Documents": [".pdf", ".docx", ".txt"],
     "Images": [".jpg", ".jpeg", ".png", ".gif"],
     "Videos": [".mp4", ".mov", ".avi"],
     "Music": [".mp3", ".wav"],
     "Archives": [".zip", ".rar"]
}

# Create destination folders if they don’t exist
for folder in file_types.keys():
    os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)

# Move files based on type
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(destination_folder, folder, file))
                print(f"Moved: {file} → {folder}")
                break
