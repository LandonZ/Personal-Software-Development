#PyQt5 Images
import sys #modules used and maintained by python interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow #import the widgets (building blocks)
from PyQt5.QtWidgets import QLabel #import the label
from PyQt5.QtGui import QPixmap #used for images and its functionality
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow): #inherit from QMainWindow

    def __init__(self):
        super().__init__()
        # sets title
        self.setWindowTitle("Images")
        # position & size of window. 0,0 means top left corner. Should have square of 500 pixels
        # 400, 350 should be around the center of the screen
        self.setGeometry(400, 350, 500, 500)
        #Label can also just be passed in w/ one argument: the window. Default label
        label = QLabel(self)
        label.setGeometry(0, 0, 480, 253) #image dimension of roaring lion
        #QPixmap constructor. Makes object with relatives/absolute file path
        pixmap = QPixmap("profile_pic.jpg")
        #set the label to the image
        label.setPixmap(pixmap)
        #image will now scale to size of label
        label.setScaledContents(True)
        # label.setAlignment(Qt.AlignCenter)
        #resetting geometry of label to middle of window.
        label.setGeometry((self.width() - label.width()) // 2, #Set to middle.
                          # // FOR INTEGER DIVISION B/C WANT PIXELS TO BE INTEGERS
                          (self.height() - label.height()) // 2, #Set to middle.
                            label.width(),
                            label.height())

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