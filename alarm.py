#Python Alarm clock

import time
import datetime
import pygame
from pkg_resources import resource_stream, resource_exists

def set_alarm(alarm_time):
    print(f"Alarm time for {alarm_time}")
    sound_file="alarm-327234.mp3"
    is_running = True

    while is_running:
        current=datetime.datetime.now().strftime("%H:%M:%S")
        print(current, end="\r")

        if current == alarm_time:
            print("Wakey... Wakey....")
            is_running = False
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)





if __name__ == '__main__':
    alarm_time=input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)