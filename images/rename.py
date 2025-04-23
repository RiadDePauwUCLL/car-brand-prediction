import os

def rename_files_in_directory(directory):
    try:
        # List all files in the directory
        for filename in os.listdir(directory):
            # Check if "Panos" is in the filename
            if "Megane" in filename:
                new_filename = filename.replace("Mégane", "Megane")  # here you choose what you want to rename
                # Get the full paths for renaming
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {filename} -> {new_filename}')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the directory
    directory_path = "./images/cars5/"
    rename_files_in_directory(directory_path)