# gui/review_widget.py
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QTextEdit, QPushButton, QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from PIL import ImageQt
import os

class ReviewWidget(QWidget):
    approved = pyqtSignal(int, str, str)  # photo_id, caption, hashtags
    
    def __init__(self):
        super().__init__()
        self.current_photo = None
        self.setup_ui()
        
    def setup_ui(self):
        layout = QHBoxLayout()
        
        # Left side - photo list
        left_panel = QVBoxLayout()
        self.photo_list = QListWidget()
        self.photo_list.itemClicked.connect(self.load_photo)
        left_panel.addWidget(QLabel("Pending Photos"))
        left_panel.addWidget(self.photo_list)
        
        # Right side - preview and editing
        right_panel = QVBoxLayout()
        
        # Image preview
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(400, 400)
        self.image_label.setStyleSheet("border: 1px solid gray")
        
        # Caption editor
        self.caption_edit = QTextEdit()
        self.caption_edit.setMaximumHeight(100)
        
        # Hashtags editor
        self.hashtags_edit = QTextEdit()
        self.hashtags_edit.setMaximumHeight(50)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.approve_btn = QPushButton("Approve")
        self.approve_btn.clicked.connect(self.approve_post)
        self.reject_btn = QPushButton("Reject")
        
        button_layout.addWidget(self.approve_btn)
        button_layout.addWidget(self.reject_btn)
        
        right_panel.addWidget(QLabel("Image Preview"))
        right_panel.addWidget(self.image_label)
        right_panel.addWidget(QLabel("Caption"))
        right_panel.addWidget(self.caption_edit)
        right_panel.addWidget(QLabel("Hashtags"))
        right_panel.addWidget(self.hashtags_edit)
        right_panel.addLayout(button_layout)
        
        layout.addLayout(left_panel, 1)
        layout.addLayout(right_panel, 2)
        self.setLayout(layout)
        
    def load_photos(self, photos):
        """Load pending photos into the list"""
        self.photo_list.clear()
        for photo in photos:
            item = QListWidgetItem(photo.filename)
            item.setData(Qt.UserRole, photo)
            self.photo_list.addItem(item)
            
    def load_photo(self, item):
        """Display selected photo for review"""
        self.current_photo = item.data(Qt.UserRole)
        
        # Load image
        pixmap = QPixmap(self.current_photo.filepath)
        scaled_pixmap = pixmap.scaled(
            self.image_label.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)
        
        # Load caption and hashtags
        self.caption_edit.setPlainText(self.current_photo.caption or "")
        self.hashtags_edit.setPlainText(self.current_photo.hashtags or "")
        
    def approve_post(self):
        if self.current_photo:
            self.approved.emit(
                self.current_photo.id,
                self.caption_edit.toPlainText(),
                self.hashtags_edit.toPlainText()
            )