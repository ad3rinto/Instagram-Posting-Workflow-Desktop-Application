# core/instagram_api.py
import requests
import os
from PIL import Image
import json

class InstagramAPI:
    def __init__(self, access_token, business_account_id):
        self.access_token = access_token
        self.business_account_id = business_account_id
        self.base_url = "https://graph.facebook.com/v18.0"
        
    def upload_media(self, image_path, caption):
        """Upload media to Instagram with retry logic"""
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                # Step 1: Upload image
                url = f"{self.base_url}/{self.business_account_id}/media"
                
                with open(image_path, 'rb') as image_file:
                    files = {
                        'image': image_file
                    }
                    params = {
                        'caption': caption,
                        'access_token': self.access_token
                    }
                    
                    response = requests.post(url, files=files, params=params)
                    result = response.json()
                    
                    if 'id' not in result:
                        raise Exception(f"Media upload failed: {result}")
                    
                    creation_id = result['id']
                    
                # Step 2: Publish media
                publish_url = f"{self.base_url}/{self.business_account_id}/media_publish"
                publish_params = {
                    'creation_id': creation_id,
                    'access_token': self.access_token
                }
                
                publish_response = requests.post(publish_url, params=publish_params)
                publish_result = publish_response.json()
                
                if 'id' in publish_result:
                    return publish_result['id']
                else:
                    raise Exception(f"Media publish failed: {publish_result}")
                    
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                time.sleep(2 ** attempt)  # Exponential backoff