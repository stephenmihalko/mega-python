import platform
import time
from datetime import datetime

hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if platform.system() == "Windows" else "/etc/hosts"
redirect = "127.0.0.1"
sites = ["www.facebook.com", "mail.google.com"]

while True:
	with open(hosts_path, "r+") as hosts:
		if datetime.now().weekday() < 5 and 8 <= datetime.now().hour < 16:
			content = hosts.read()
			for site in sites:
				if site in content:
					pass
				else:
					file.write(redirect + " " + site + "\n")
