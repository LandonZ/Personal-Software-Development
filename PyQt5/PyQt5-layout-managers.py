#PyQt5 layout managers
import sys #modules used and maintained by python interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow #import the widgets (building blocks)
#import these classes that deal with layout managers
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

class MainWindow(QMainWindow): #inherit from QMainWindow

    def __init__(self):
        super().__init__()
        # sets title
        self.setWindowTitle("Layout Managers")
        # position & size of window. 0,0 means top left corner. Should have square of 500 pixels
        # 400, 350 should be around the center of the screen
        self.setGeometry(400, 350, 500, 500)
        self.initUI()

    #separate function to initialize the UI once constructed (to keep clutter)
    def initUI(self):
        central_widget = QWidget() #construct the central widget of window
        # sets central widget to window.
        # now when working with layout managers, add these to central widget, which is then added
        # to the main window.
        self.setCentralWidget(central_widget)

        label1 = QLabel('#1', self)
        label2 = QLabel('#2', self)
        label3 = QLabel('#3', self)
        label4 = QLabel('#4', self)
        label5 = QLabel('#5', self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")
        #AT THIS POINT, ALL LABELS ARE OVERLAPPING EACH OTHER.

        # --- LAYOUT MANAGER TYPES ---
        # QVBoxLayout() = label gets its own "Vertical Box"
        # QHBoxLayout() = each label gets own "Horizontal Box"
        # QGridLayout() = each label gets own customized grid (NEED TO SPECIFY)
        ''' FOR THE VBOX
        vbox = QVBoxLayout()
        #add all the widgets to the vbox
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        #now, set the central widget layout manager to vbox.
        central_widget.setLayout(vbox)
        '''

        #GRID
        grid = QGridLayout()
        #specify the ROW AND COLUMN for each label
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        #bottom right (last row and col cell)
        grid.addWidget(label5, 2, 2)

        central_widget.setLayout(grid)

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