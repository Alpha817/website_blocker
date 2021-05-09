from datetime import datetime
end_time = datetime(2021,5,9,20)
sites_to_block = ["www.facebook.com","facebook.com"]
hosts_path = r"\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
def block_sites():
    if datetime.now() < end_time:
        print("Block sites")
        with open (hosts_path,"r+") as hostsfile:
            hosts_content = hostsfiles.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostfile.write (redirect+ " "+ site+ "\n")
    else:
        print ("unblock sites")
        with open (hosts_path, "r") as hostfile:
            lines = hostfiles.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any (site in line for site in sites_to_block):
                    hostsfile.write(line)
            hostsfile.read.truncate()
if __name__ == "__main__":
    block_sites()
