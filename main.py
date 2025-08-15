# main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from database.models import init_db

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())