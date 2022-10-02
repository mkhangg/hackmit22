# Import neccessary libraries
from tuning import Tuning
import usb.core
import usb.util
import time

# voice detected flag
flag_detected = 0

# file spec & open file
filePath = './output.txt'
fileName = open("output.txt", "w")

# define usb
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

if dev:
    Mic_tuning = Tuning(dev)
    if Mic_tuning.is_voice():
        # print(Mic_tuning.is_voice())
        # print(360 - Mic_tuning.direction)
        print("Detecting...")
        
    while True:
        try:
            if flag_detected:
                # print to terminal 
                print("Voice detected!")
                
                exit(0)
                
            if Mic_tuning.is_voice():
                # print(Mic_tuning.is_voice())
                direction = int(360 - Mic_tuning.direction)
                
                # print to terminal & write to file & close file
                print("angle = ", direction)
                fileName.write("%d" %direction)
                fileName.close()
                
                # set flag as detected
                flag_detected = 1
                
            time.sleep(1)
            
        except KeyboardInterrupt:
            break
