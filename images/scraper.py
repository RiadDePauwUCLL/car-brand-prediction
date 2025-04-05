from dotenv import load_dotenv
import requests
import os

load_dotenv(".env",override=True)

API_KEY = os.getenv('API_key')
BASE_URL = 'https://api.pexels.com/v1/'

class PexelsApiSearch:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
    
    def search(self, query, per_page=15):
        headers = {'Authorization': self.api_key}
        params = {'query': query, 'per_page': per_page}
        response = requests.get(self.base_url + 'search', \
                                headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return [photo['src']['original'] for photo in data['photos']]
        else:
            print('Error:', response.status_code)
            return []

    def save_images(self, image_urls, query):
        save_directory = f'./data/scraped/{query}'
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        for i, url in enumerate(image_urls):
            response = requests.get(url)
            if response.status_code == 200:
                file_path = os.path.join(save_directory, f'image_{i+1}.jpg')
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f'Saved: {file_path}')
            else:
                print(f'Error downloading image {i+1}:',response.status_code)

def main():
    search_query = input('Enter a search term: ')
    num_images = int(input('Enter the number of images to search for: '))

    pexels_api_search_service = PexelsApiSearch()

    image_urls_list = pexels_api_search_service.search(search_query,num_images)
    if image_urls_list:
        pexels_api_search_service.save_images(image_urls_list, search_query)

if __name__ == '__main__':
    main()