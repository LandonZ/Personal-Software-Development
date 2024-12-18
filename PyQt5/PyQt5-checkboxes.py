#PyQt5 checkboxes
import sys #modules used and maintained by python interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow #import the widgets (building blocks)
from PyQt5.QtWidgets import QCheckBox #import the checkbox module
from PyQt5.QtCore import Qt #need relevant for Qt classes- nonclasses modules

class MainWindow(QMainWindow): #inherit from QMainWindow

    def __init__(self):
        super().__init__()
        # sets title
        self.setWindowTitle("Checkboxes")
        # position & size of window. 0,0 means top left corner. Should have square of 500 pixels
        # 400, 350 should be around the center of the screen
        self.setGeometry(400, 350, 500, 500)
        #Parameters: text of checkbox, then the window
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    #setting style
    def initUI(self):
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Times New Roman;")
        self.checkbox.setGeometry(10, 0, 500, 100)
        #set initial state of checkbox
        self.checkbox.setChecked(False)
        #connect the signal with the function
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    #function for when checkbox changed. state parameter provided when interacted w/ checkbox
    # STATE: 0 - unchecked, 1- partially checked, 2- checked
    def checkbox_changed(self, state):
        if state == Qt.Checked: #Qt.Checked is 2 constant
            print("You like food")
        else:
            print("You don't like food")


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