#PyQt5 buttons
import sys #modules used and maintained by python interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow #import the widgets (building blocks)
from PyQt5.QtWidgets import QPushButton, QLabel #import the button module

class MainWindow(QMainWindow): #inherit from QMainWindow

    def __init__(self):
        super().__init__()
        # sets title
        self.setWindowTitle("Buttons")
        # position & size of window. 0,0 means top left corner. Should have square of 500 pixels
        # 400, 350 should be around the center of the screen
        self.setGeometry(400, 350, 500, 500)

        # PARAMETERS: the text of button, then the window
        # Should be SELF.BUTTON so button spans to on_click function and not just local variable
        # This should be in your constructor when initializing everything in window frame.
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    #setting style
    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        #CONNECT when button clicked to the function. No parentheses for on_click function
        #A signal connected to the slot (the action the button's gonna take)
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    # button on click function
    def on_click(self):
        print("Button clicked!")
        self.label.setText("Goodbye!")
        #set the button text
        self.button.setText("Clicked!")
        #disable the button
        self.button.setDisabled(True)

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