import os
import sys
import time
import datetime
import threading
from tqdm import tqdm

def setprop():
    commands = ["adb shell -s localhost wm size 1080x1920",
                "adb shell -s localhost wm density 440"]
    for cmd in commands:
        os.system(cmd)

def check_device(keyword,flag):
    cmd = "adb devices"
    t1 = datetime.datetime.now()
    while True:
        os.system("adb connect localhost")
        results = os.popen(cmd).read()
        t2 = datetime.datetime.now()
        if (t2-t1).seconds > 120: #* Timeout 120 seconds
            print("Error: Devices connect Timeout")
            flag = False
            return flag
        else:
            if keyword not in results:
                print("Devices is not online...")
                time.sleep(1)
                continue
            else:
                print("Devices is online will set size and density")
                waittingBar()
                print("Waitting...")
                setprop()
                return flag

def waittingBar():
    for i in tqdm(range(1,6)):
        time.sleep(1)

def start_civ():
    cmd = "sudo -E /home/cfc/civ/scripts/start_civ.sh -g VirtIO"
    os.system(cmd)

def main():
    flag = True
    keyword = "localhost:5555\tdevice"
    T1 = threading.Thread(target=check_device, args=(keyword,flag))
    T2 = threading.Thread(target=start_civ,)
    T2.start()
    T1.start()



if __name__ == '__main__':
    main()