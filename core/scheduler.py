# core/scheduler.py
from datetime import datetime, timedelta
from database.models import Session, Photo
import schedule
import time
from threading import Thread
from core.instagram_api import InstagramAPI

class PostScheduler:
    def __init__(self, instagram_api):
        self.api = instagram_api
        self.session = Session()
        self.running = False
        
    def schedule_post(self, photo_id, schedule_time=None):
        """Schedule a photo for posting"""
        if not schedule_time:
            # Default to next 12 PM
            now = datetime.now()
            schedule_time = now.replace(hour=12, minute=0, second=0, microsecond=0)
            if schedule_time < now:
                schedule_time += timedelta(days=1)
                
        photo = self.session.query(Photo).get(photo_id)
        if photo:
            photo.scheduled_time = schedule_time
            photo.status = 'approved'
            self.session.commit()
            
    def start_scheduler(self):
        """Start the background scheduler"""
        self.running = True
        schedule.every().day.at("12:00").do(self.publish_scheduled_posts)
        
        def run_scheduler():
            while self.running:
                schedule.run_pending()
                time.sleep(60)
                
        Thread(target=run_scheduler, daemon=True).start()
        
    def publish_scheduled_posts(self):
        """Publish all scheduled posts for today"""
        today = datetime.now().date()
        scheduled_photos = self.session.query(Photo).filter(
            Photo.status == 'approved',
            Photo.scheduled_time >= today,
            Photo.scheduled_time < today + timedelta(days=1)
        ).all()
        
        for photo in scheduled_photos:
            try:
                full_caption = f"{photo.caption}\n\n{photo.hashtags}"
                post_id = self.api.upload_media(photo.filepath, full_caption)
                
                photo.status = 'posted'
                photo.instagram_post_id = post_id
                photo.posted_time = datetime.now()
                self.session.commit()
                
            except Exception as e:
                photo.status = 'failed'
                self.session.commit()
                print(f"Failed to post {photo.filename}: {e}")