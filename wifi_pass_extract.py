import subprocess
from datetime import datetime
from time import sleep

#Banner
print("\n"+"#"*65)
print("#\tWelcome to V WiFi Password Extractor for Windows\t#\n#\t\t\t\t\t\t\t\t#")
print("#\tVisit: https://hackwithv.blogspot.com/\t\t\t#\n#\t\t\t\t\t\t\t\t#")
print("#\tTime started at\t: "+str(datetime.now())+"\t\t#")
print("#"*65+"\n\n")

#Disclaimer
print("Disclaimer: Developer assume no liability and are not responsible\n\t    for any misuse or damage caused by this tool.\n\n")

ex=input("[+] Press Enter key to Start...")

#Agree
ag = 'null'
ag = input("\n[!] Use this tool for educational purpose only\n[?] Are you agree? [ Y / N ] : ")
if ag == 'y' or ag =='Y':
        pass
else:
        print("\n[-] Please agree the tool, try again!")
        ex=input("\n[!] Press Enter key to exit... ")
        print("\n[+] Thanks for using V WiFi Password Extractor Tool\n")
        sleep(2)
        exit()

#netsh process
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n') 
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print("\n+{:<20}+{:<}+".format("-"*30, "-"*32))
print("{:<24} | {:<} \t\t|".format("|\tNetwork Name", "\tPassword"))
print("+{:<20}+{:<}+".format("-"*30, "-"*32))

for i in profiles:
	try: 
		results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n') 
		results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
		
		try:
			print ("{:<24} | {:<} \t\t|".format("|\t"+i, "\t"+results[0]))
		except IndexError:
			print ("{:<24} | {:<} \t\t|".format("|\t"+i, "\t\t"))
	except subprocess.CalledProcessError:
		print ("{:<24} | {:<} \t\t|".format("|\t"+i, "\tENCODING ERROR"))
print("+{:<20}+{:<}+".format("-"*30, "-"*32))
#End of netsh

ex=input("\n\n[!] Press Enter key to exit... ")
print("\n[+] Thanks for using V WiFi Password Extractor Tool\n")
sleep(3)
exit()
