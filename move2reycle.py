# Copyright (c) 2026 Khushaldas Vasant Badhan
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.

def your_script_function():
    # Your code starts here...
    pass

import os
import sys
from send2trash import send2trash

def move_files_to_recycle_bin(target_paths, extensions):
    """
    Moves files with specific extensions from provided directories 
    (and their subfolders) to the Recycle Bin/Trash.
    
    :param target_paths: A list of directory paths (strings) or a single path string.
    :param extensions: A list of extensions (e.g., ['.txt', 'jpg']) or a single extension.
    """
    
    # Normalize inputs to lists
    if isinstance(target_paths, str):
        target_paths = [target_paths]
    if isinstance(extensions, str):
        extensions = [extensions]

    # Ensure extensions are lowercase and start with a dot for comparison
    clean_exts = []
    for ext in extensions:
        clean_ext = ext.lower()
        if not clean_ext.startswith('.'):
            clean_ext = '.' + clean_ext
        clean_exts.append(clean_ext)
    
    clean_exts = tuple(clean_exts) # endswith accepts a tuple
    files_moved_count = 0
    errors_count = 0

    print(f"--- Starting cleanup ---")
    print(f"Target Extensions: {clean_exts}")

    for folder_path in target_paths:
        if not os.path.exists(folder_path):
            print(f"Skipping: Directory not found -> {folder_path}")
            continue

        print(f"Scanning: {folder_path}")

        # os.walk allows us to look into subfolders recursively
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                # Check extension (case insensitive)
                if filename.lower().endswith(clean_exts):
                    file_path = os.path.join(root, filename)
                    
                    try:
                        print(f"Trashing: {file_path}")
                        
                        # This performs the action of moving to Recycle Bin
                        send2trash(file_path)
                        
                        files_moved_count += 1
                    except Exception as e:
                        print(f"ERROR moving {file_path}: {e}")
                        errors_count += 1

    print("-" * 30)
    print(f"Completed.")
    print(f"Total files moved to trash: {files_moved_count}")
    print(f"Total errors: {errors_count}")

# ==========================================
# Configuration Area
# ==========================================
if __name__ == "__main__":
    # 1. Define the directories you want to clean
    # You can use raw strings (r"path") to handle backslashes on Windows easily
    directories_to_clean = [
        r"C:\Users\User\Documents\folder"
    ]

    # 2. Define the extensions to remove
    # (Format can be "txt" or ".txt")
    file_extensions = [".cpp"]

    # 3. Run the function
    # Only run if there are directories listed to prevent accidents
    if directories_to_clean:
        move_files_to_recycle_bin(directories_to_clean, file_extensions)
    else:
        print("Please configure the 'directories_to_clean' list in the script.")
