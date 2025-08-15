# core/photo_scanner.py
import os
from PIL import Image
from database.models import Photo, Session

class PhotoScanner:
    def __init__(self, watch_folder):
        self.watch_folder = watch_folder
        self.session = Session()
        
    def scan_new_photos(self):
        """Scan folder for new JPEG/PNG images"""
        supported_formats = ('.jpg', '.jpeg', '.png')
        existing_files = {p.filename for p in self.session.query(Photo).all()}
        
        new_photos = []
        for filename in os.listdir(self.watch_folder):
            if filename.lower().endswith(supported_formats) and filename not in existing_files:
                filepath = os.path.join(self.watch_folder, filename)
                try:
                    # Validate image
                    with Image.open(filepath) as img:
                        img.verify()
                    
                    photo = Photo(
                        filename=filename,
                        filepath=filepath,
                        status='pending'
                    )
                    self.session.add(photo)
                    new_photos.append(photo)
                except Exception as e:
                    print(f"Invalid image {filename}: {e}")
        
        self.session.commit()
        return new_photos