#PyQt5 line edits
import sys #modules used and maintained by python interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow #import the widgets (building blocks)
from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout #import button, widget, layout manage

class MainWindow(QMainWindow): #inherit from QMainWindow

    def __init__(self):
        super().__init__()
        # sets title
        self.setWindowTitle("CSS Styles")
        # DONT NEED setGeometry OF WINDOW. Because using layout manager

        #since using layout manager don't need to add self to window.
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    #setting style
    def initUI(self):
        #set central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        #create layout manager and add widgets to it
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        #set the layout for the central widget
        central_widget.setLayout(hbox)

        #set the name of each button. Refer to these names in CSS sheet
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        #general css layout sheet for window.
        #Styles applying to all buttons
        #then, styles applying to specific buttons

        #padding: pixels between text and border
        #15px top and bottom, 75px sides
        #margin: space around the whole widget
        #border: width of 3px, and is solid
        #border-radius: make rounded with pixel curvature
        #colors: can use hex, rgb, or hsl. Search up color picker
        #HSL USEFUL BC CAN UP THE LIGHTNESS- hue, saturation, lightness

        #hover- properties applied when hovering over buttons
        #will make button lighter, increasing third param of hsl
        self.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            font-family: Times New Roman;
            padding: 15px 75px;
            margin: 25px;
            border: 3px solid;
            border-radius: 15px;
        }
        QPushButton#button1{
            background-color: hsl(353, 60%, 50%);
        }
        QPushButton#button2{
            background-color: hsl(136, 55%, 49%);
        }
        QPushButton#button3{
            background-color: hsl(189, 61%, 48%);
        }
        QPushButton#button1:hover{
            background-color: hsl(353, 60%, 70%);
        }
        QPushButton#button2:hover{
            background-color: hsl(136, 55%, 69%);
        }
        QPushButton#button3:hover{
            background-color: hsl(189, 61%, 68%);
        }
        """)


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