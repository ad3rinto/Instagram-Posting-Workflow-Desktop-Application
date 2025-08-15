# core/caption_generator.py
import openai
import os
from PIL import Image
import base64
from io import BytesIO

class CaptionGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key
        
    def generate_caption(self, image_path):
        """Generate Instagram caption with hashtags"""
        # Convert image to base64
        with Image.open(image_path) as img:
            buffer = BytesIO()
            img.save(buffer, format='JPEG')
            img_b64 = base64.b64encode(buffer.getvalue()).decode()
        
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Generate an engaging Instagram caption for this photo. 
                            Include relevant hashtags and optimize for engagement. 
                            Keep it under 150 words. Format as:
                            Caption: [engaging caption]
                            Hashtags: [#hashtag1 #hashtag2 ...]"""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{img_b64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=150
        )
        
        content = response.choices[0].message.content
        caption_part = content.split("Hashtags:")[0].replace("Caption:", "").strip()
        hashtags_part = content.split("Hashtags:")[1].strip()
        
        return {
            'caption': caption_part,
            'hashtags': hashtags_part
        }