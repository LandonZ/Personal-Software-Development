#PyQt5 GUI intro
import sys #modules used and maintained by python interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow #import the widgets (building blocks)
from PyQt5.QtGui import QIcon #import the icon
from PyQt5.QtWidgets import QLabel #import the label
from PyQt5.QtGui import QFont #import the font
from PyQt5.QtCore import Qt #Qt used for alignments

class MainWindow(QMainWindow): #inherit from QMainWindow

    def __init__(self):
        super().__init__()
        # sets title
        self.setWindowTitle("My cool first GUI")
        # position & size of window. 0,0 means top left corner. Should have square of 500 pixels
        # 400, 350 should be around the center of the screen
        self.setGeometry(400, 350, 500, 500)
        #Set window icon, creating new QIcon constructor with relative/absolute file path.
        #Window icon not seen on mac
        self.setWindowIcon(QIcon("profile_pic.jpg"))
        #Label object. First the "message", then the window object self
        label = QLabel("Hello", self)
        #set font of the label. Font, then font size
        label.setFont(QFont("Times New Roman", 40))
        #set position and size. top left corner, width 500 height 100
        label.setGeometry(0, 0, 500, 100)
        #Can set style to label, similar to CSS. end with semicolon
        label.setStyleSheet("color: #3dd47e;" #light pastel green
                            "background-color: #404743;" #gray background
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;"
                            )
        #Align the text vertically and horizontally to center with Qt class
        #use bitwise or operator to use both features
        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        # OR CAN USE: Qt.AlignCenter as just center general


def main():
    # create QApp object with argument sys.argv
    # this argument gives the script name.
    # allows PyQt to process any command like arguments (terminal)
    app = QApplication(sys.argv)
    # window object. Default behavior: hide window
    window = MainWindow()
    # shows the window, but will disappear right after
    window.show()
    # ensures clean exit of program.
    # app.exec_ waits for user input and events.
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


