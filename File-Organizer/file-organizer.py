# File Organizer Organizer
import os
import shutil

FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pdf'],
    'Audio': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mov'],
    'WinRAR': ['.zip'],
    'Programs': ['.py', '.html', '.css', '.js', '.jsx']
}

path = input("Enter folder path: ")
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    
    if os.path.isfile(file_path):
        ext = '.' + file.split('.')[-1].lower()
        
        for folder, extensions in FOLDERS.items():
            if ext in extensions:
                
                dest = os.path.join(path, folder)
                os.makedirs(dest, exist_ok=True)
                shutil.move(file_path, os.path.join(dest, file))
                print(f"Moved {file} to {folder}")
                

