from icrawler.builtin import GoogleImageCrawler
import os
import glob
import shutil

def scrape_images(search_term, max_images):
    # Create the directory path for this search term
    dir_path = os.path.join('./images/googlescrape', search_term)
    
    # Ensure the directory exists
    os.makedirs(dir_path, exist_ok=True)
    
    # Initialize the crawler with the specific directory
    google_crawler = GoogleImageCrawler(storage={'root_dir': dir_path})
    
    # Crawl images for the search term
    google_crawler.crawl(keyword=search_term, max_num=max_images)
    
    # Rename the downloaded files
    rename_images(dir_path, search_term)
    
    print(f"Saved and renamed {max_images} images for '{search_term}' to {dir_path}")

def rename_images(directory, search_term):
    # Get a list of all image files in the directory
    image_files = []
    for ext in ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.webp']:
        image_files.extend(glob.glob(os.path.join(directory, ext)))
    
    # Create a temp directory for the renaming process
    temp_dir = os.path.join(directory, 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    
    # Rename each file
    for i, file_path in enumerate(image_files):
        # Get the file extension
        _, ext = os.path.splitext(file_path)
        
        # Create the new filename
        new_filename = f"{search_term}_{i+1}{ext}"
        new_path = os.path.join(temp_dir, new_filename)
        
        # Copy to temp directory with the new name
        shutil.copy2(file_path, new_path)
    
    # Delete original files
    for file_path in image_files:
        os.remove(file_path)
    
    # Move renamed files back to original directory
    for file_name in os.listdir(temp_dir):
        shutil.move(os.path.join(temp_dir, file_name), os.path.join(directory, file_name))
    
    # Remove temp directory
    os.rmdir(temp_dir)

# Example usage:
scrape_images('sports car', 65)