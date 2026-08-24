import os
import shutil
import sys


def copy_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Loop through each item in the source directory
    for folder_name in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder_name)

        # Only process folders
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder_name}")

            # Loop through files inside the folder
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                # Only copy files
                if os.path.isfile(file_path):
                    destination_path = os.path.join(destination_dir, file_name)

                    shutil.copy2(file_path, destination_path)
                    print(f"Copied: {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python copy_files.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    copy_files(source_directory, destination_directory)