import sys

from PySide6.QtWidgets import QApplication

from app import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
