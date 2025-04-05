import os
import shutil
import random
import string

def group_and_cleanup_images(parent_directory, destination_folder_name="scraped_images"):
    """
    Groups all images from all folders within parent_directory (except the destination folder)
    into the destination folder with random names. Then deletes all source folders.

    Args:
        parent_directory (str): Parent directory containing all image folders
        destination_folder_name (str): Name of the destination folder within parent_directory
    """
    # Full path to destination folder
    destination_folder = os.path.join(parent_directory, destination_folder_name)
    
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    
    # Find all subdirectories in the parent directory
    source_folders = []
    for item in os.listdir(parent_directory):
        item_path = os.path.join(parent_directory, item)
        if os.path.isdir(item_path) and item != destination_folder_name:
            source_folders.append(item_path)
    
    print(f"Found {len(source_folders)} source folders to process")
    
    # Track statistics
    total_images_copied = 0
    
    # Process each folder
    for folder in source_folders:
        folder_images = 0
        for root, _, files in os.walk(folder):
            for file in files:
                # Check if the file is an image (by extension)
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                    source_path = os.path.join(root, file)
                    
                    # Get the file extension
                    _, extension = os.path.splitext(file)
                    
                    # Generate a random name (12 characters + extension)
                    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12)) + extension
                    
                    # Make sure the random name is unique
                    while os.path.exists(os.path.join(destination_folder, random_name)):
                        random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12)) + extension
                    
                    destination_path = os.path.join(destination_folder, random_name)
                    
                    # Copy the file to destination
                    try:
                        shutil.copy2(source_path, destination_path)
                        folder_images += 1
                        total_images_copied += 1
                    except Exception as e:
                        print(f"Error copying {source_path}: {e}")
        
        print(f"Copied {folder_images} images from {folder}")
        
        # Delete the source folder after copying all images
        try:
            shutil.rmtree(folder)
            print(f"Deleted source folder: {folder}")
        except Exception as e:
            print(f"Error deleting folder {folder}: {e}")
    
    print(f"Total images consolidated: {total_images_copied}")
    print(f"All images are now in: {destination_folder}")

if __name__ == "__main__":
    # Define the parent directory
    parent_dir = r"x:\School\Year 2\Semester 2\Advanced AI\projects\car-price-predictions\data"
    
    # Run the consolidation process
    group_and_cleanup_images(parent_dir)