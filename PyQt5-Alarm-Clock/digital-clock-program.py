#Python PyQt5 Digital Clock
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt #Qt is for alignment
from PyQt5.QtGui import QFont, QFontDatabase #to work with specific fonts

class DigitalClock(QWidget): #inherit from the widget b/c digitalclock will be a widget
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(400, 350, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label) #add label to layout manager
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter) #vertically and horizontally align center

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(136, 82%, 48%);")
        self.setStyleSheet("background-color: black;")
        '''
        FONT DOESN'T WORK.
        
        #has database of all fonts for application. Add this font to it
        font_id = QFontDatabase.addApplicationFont("DIGIT.TTF")
        if font_id == -1:
            print("Failed to load font")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0] #get font family
        my_font = QFont(font_family, 150) #QFont for font family then the size
        self.time_label.setFont(my_font) #set the font for the label now
        '''

        # during signal timeout, update time (every 1000 ms)
        self.timer.timeout.connect(self.update_time)
        #start the timer and trigger every 1000 ms
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        #get current time toString format. AP means AM/PM
        self.time_label.setText(current_time) #set label text to the time

if __name__ == '__main__':
    app = QApplication(sys.argv) #creates the app. sys.argv for running from terminal
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_()) #makes window not disappear