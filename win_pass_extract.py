import subprocess
from datetime import datetime

#Banner
print("-"*70)
print("\t\tWelcome to V Wifi Password Extractor for Windows\n")
print("\tTime started at\t: "+str(datetime.now()))
print("-"*70,"\n\n")

#netsh process
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n') 
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i] 

print("{:<30} | {:<}".format("Network Names", "Passwords"))
print("{:<30}|{:<}".format("-"*31, "-"*25))

for i in profiles:
	try: 
		results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n') 
		results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
		
		try:
			print ("{:<30} | {:<}".format(i, results[0]))
		except IndexError:
			print ("{:<30}| {:<}".format(i, ""))
	except subprocess.CalledProcessError:
		print ("{:<30}| {:<}".format(i, "ENCODING ERROR"))
#End of netsh
print("\n\nThanking you, Bye !\n")
