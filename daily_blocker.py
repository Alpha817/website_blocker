import time
from datetime import datetime as dt
hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["instagram.com", "www.instagram.com", "arshbir588@gmail.com","www.arshbir588@gmail.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            print(content)
    else:
        print("Fun Hours")
    time.sleep(5)