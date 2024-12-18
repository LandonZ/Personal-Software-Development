#PyQt5 line edits
import sys #modules used and maintained by python interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow #import the widgets (building blocks)
from PyQt5.QtWidgets import QLineEdit, QPushButton #import line edit module

class MainWindow(QMainWindow): #inherit from QMainWindow

    def __init__(self):
        super().__init__()
        # sets title
        self.setWindowTitle("Line Edits")
        # position & size of window. 0,0 means top left corner. Should have square of 500 pixels
        # 400, 350 should be around the center of the screen
        self.setGeometry(400, 350, 500, 500)
        #construct line edit wdiget
        self.line_edit = QLineEdit(self)
        #use button to submit when line edit is done typing
        self.button = QPushButton("Submit", self)

        self.initUI()

    #setting style
    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Times New Roman;")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Times New Roman;")
        #setting placeholder text
        self.line_edit.setPlaceholderText("Enter your name: ")
        #connect signal of clicked to connect of the function
        self.button.clicked.connect(self.submit)

    def submit(self):
        #get text in line edit
        text = self.line_edit.text()
        print(f"{text}, you're weird")


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