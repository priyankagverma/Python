# import time
# from plyer import notification

# while True:
#     print("Please take a break!")
#     notification.notify(title="Please get some rest", message="Take 30 seconds break",)
#     time.sleep(3)

import subprocess
import time

while True:
    subprocess.run([
        "osascript",
        "-e",
        'display notification "Take a 30 second break! You have been coding all day!!" with title "Please get some rest"'
    ])
    time.sleep(3600)



