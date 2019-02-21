import platform
import time
from datetime import datetime

hosts_path = "hosts"
#hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if platform.system() == "Windows" else "/etc/hosts"
redirect = "127.0.0.1"
sites = ["www.facebook.com", "mail.google.com"]

while True:
	with open(hosts_path, "r+") as hosts:
		# If Monday-Friday (0-5) and between 8a and 4p
		if datetime.now().weekday() < 5 and 8 <= datetime.now().hour < 20:
			content = hosts.read()
			# Check to see if each site is in the content.
			for site in sites:
				# This is "continue" in other languages.
				if site in content:
					pass
				# Put the site in the file.
				else:
					hosts.write(redirect + " " + site + "\n")
		else:
                        # Read the lines into a list of strings this time
                        content = hosts.readlines()
                        # Start the cursor at the beginning of the file
                        hosts.seek(0)
                        # Go through each line in the list to check for sites
                        for line in content:
                                if not any(website in line for website in sites):
                                        hosts.write(line)
                        # Cut everything off after the stuff we wrote
                        hosts.truncate()

	# Wait a minute so as not to tax resources.
	time.sleep(60)
