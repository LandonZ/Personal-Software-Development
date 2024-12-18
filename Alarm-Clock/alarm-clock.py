#PYTHON ALARM CLOCK
import time #time class
import datetime
import pygame #sound effects

def set_alarm(alarm_time): #string representation of time in military time
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3" #relative file
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        #getting hours, min, and secs only
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 🤣")

            pygame.mixer.init() #initializes mixer to play sound, another way to called constructor
            pygame.mixer.music.load(sound_file) #module pygame, mixer, music
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy(): #if song is busy/still playing
                time.sleep(1)

            is_running = False

        time.sleep(1) #sleeps program for 1 second

if __name__ == '__main__':
    alarm_time = input("Enter the alarm time (HH:MM:SS) MILITARY TIME: ")
    set_alarm(alarm_time)