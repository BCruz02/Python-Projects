import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awsome First GUI")
        self.setGeometry(700,300, 500, 600)
        self.button = QPushButton("Click If Your Awsome!", self)
        self.setWindowIcon(QIcon(r"C:\Users\Bcbra\PythonProject\SmallPythonProjects.py\Pic_For_GUI.jpg"))
        self.initUI()

        label = QLabel("Hello Coders", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: blue;"
                            "background-color: orange;")
        
        label.setAlignment(Qt.AlignCenter)

    def initUI(self):
        
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 20px;")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("You Are Indeed Awsome!")
        self.button.setText("Clicked!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()