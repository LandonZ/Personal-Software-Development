# openweathermap.org
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QVBoxLayout)
from PyQt5.QtCore import Qt
from requests import RequestException


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self) #for the city
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)
        #to center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        #for css
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # pound sign objectname used for objects falling under that class only
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
                min-height: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "1582ea1ee2ca990b846d5f0ee92c7a61"
        city = self.city_input.text() #get the city typed in
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url) #requests to call api
            response.raise_for_status() #will manually raise an exception if any HTTP errors.
            data = response.json() #convert to json

            if data["cod"] == 200: #if request was successful
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            #when HTTP returns code 400-500 (client/server error)
            match response.status_code: #switch
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeou:t\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            #network problems, invalid urls, etc
            self.display_error(f"Request Error:\n{req_error}")


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;") #change font size
        self.temperature_label.setText(message)
        #clear emoji and description
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;") #reset font size
        # -- TEMPERATURE --
        # data contains 'main' key that contains a dictionary with a 'temp' key in kelvin
        temperature_k = data["main"]["temp"]
        temperature_f = (temperature_k * 9 / 5) - 459.67

        # -- DESCRIPTION --
        # data contains 'weather' key that contains a list, index 0 having a
        # dictionary with key 'description'
        weather_description = data["weather"][0]["description"]

        # -- WEATHER ID FOR EMOJI --
        # 'weather' key in list index 0 has dictionary with key 'id'.
        # this id number relates to what type of weather it is
        # 2xx: thunderstorm, 3xx: drizzle, 5xx: rain,
        # 6xx: snow, 7xx: atmosphere, 800: clear sky, 80x: clouds
        weather_id = data["weather"][0]["id"]

        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id)) #get emoji and set text
        self.description_label.setText(weather_description)

    #static class method
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id < 232: #thunderstorm
            return "⛈️"
        elif 300 <= weather_id <= 321: #partially cloudy sky
            return "🌦️"
        elif 500 <= weather_id <= 531: #rain
            return "🌧️"
        elif 600 <= weather_id <= 622: #snow
            return "❄️"
        elif 701 <= weather_id <= 741: #mist/fog
            return "🌫️"
        elif weather_id == 762: #volcano
            return "🌋"
        elif weather_id == 771: #violent gust of wind
            return "💨"
        elif weather_id == 781: #return tornado
            return "🌪️"
        elif weather_id == 800: #clear sky
            return "☀️"
        elif 801 <= weather_id <= 804: #clouds
            return "☁️"
        else:
            return ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weatherApp = WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_())
