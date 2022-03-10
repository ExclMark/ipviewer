import requests, sys, os, re
from time import sleep

__version__ = 0.2

def clear_screen():
	sleep(0.7)
	if sys.platform == "win32" or sys.platform == "win64":
		os.system("cls")
	if sys.platform == "darwin" or sys.platform == "linux" or sys.platform == "linux2":
		os.system("clear")

def check_update():
	# Check for newer version of ipviewer
    try:
        r = requests.get("https://raw.githubusercontent.com/ExclMark/ipviewer/ipviewer.py")

        remote_version = str(re.findall('__version__ = "(.*)"', r.text)[0])
        local_version = __version__

        if remote_version != local_version:
            print("\033[93mUpdate Available!\n" +
                  f"You are running version \033[96m{local_version}\033[93m. Version \033[96m{remote_version}\033[93m is available at \033[96m\033[1m\033[4mhttps://github.com/ExclMark/ipviewer\033[0m")

    except Exception as error:
        print(f"\033[91mA problem occurred while checking for an update: {error}")

def get_info(ip):
	try:
		# Clearing terminal
		clear_screen()
		print(f"\033[96m\033[1mChecking info about \033[94m\033[1m{ip}\033[96m\033[1m:\033[0m")

		# Requesting for ip details
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		ip = response.get("query")
		region = response.get("region")
		region_name = response.get("regionName")
		isp = response.get("isp")
		org = response.get("org")
		country = response.get("country")
		city = response.get("city")
		zip_ = response.get("zip")
		lat = response.get("lat")
		lon = response.get("lon")
		tz = response.get("timezone")

		print("")
		print(f"\033[96m  > \033[0m[\033[92mCOUNTRY\033[0m]:           \033[94m\033[1m{country}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mREGION\033[0m]:            \033[94m\033[1m{region}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mREGION NAME\033[0m]:       \033[94m\033[1m{region_name}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mCITY\033[0m]:              \033[94m\033[1m{city}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mZIP POSTAL CODE\033[0m]:   \033[94m\033[1m{zip_}\033[0m")
		print("")
		print(f"\033[96m  > \033[0m[\033[92mISP\033[0m]:               \033[94m\033[1m{isp}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mORGANIZATION\033[0m]:      \033[94m\033[1m{org}\033[0m")
		print("")
		print(f"\033[96m  > \033[0m[\033[92mLATITUDE\033[0m]:          \033[94m\033[1m{lat}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mLONGITUDE\033[0m]:         \033[94m\033[1m{lon}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mTIMEZONE\033[0m]:          \033[94m\033[1m{tz}\033[0m")
		print("")
		y = input("\033[96m\033[1mView map? [y/n]: \033[0m")
		if y.lower() == "y":
			url = f"https://www.google.com/maps/search/?api=1&query={lat}%2C{lon}"
			print(f"\033[96m\033[4m{url}\n\033[0m\033[92mHold \033[4mctrl\033[0m\033[92m and click on url to open browser.")
			print("")
			sleep(1)
			print(input("\033[0mPress enter to return to home screen... \033[0m"))
			clear_screen()
			logo()
		else:
			clear_screen()
			logo()
	except requests.exceptions.ConnectionError:
		print("\033[93m\033[1m[!] CONNECTION ERROR! Please, check your internet connection.\033[0m")
		print(input("Press enter to return to home screen... "))
		clear_screen()
		logo()
	except KeyboardInterrupt:
		print("\n\033[94m\033[1mBye!\033[0m")
		sys.exit()

def query():
	print("\033[92mSelect option:")
	print("\033[94m 1 > \033[96mView my ip info")
	print("\033[94m 2 > \033[96mView target ip info")
	print("\033[94m 9 > \033[96mExit")
	return input("\033[92m>>>\033[0m ")

def logo():
	# Printing logo
	print("\033[1m")
	print("\033[94m ___    \033[96m__     ___                        ")
	print("\033[94m|_ _|_ _\033[96m\ \   / (_) _____      _____ _ __ ")
	print("\033[94m | || '_ \033[96m\ \ / /| |/ _ \ \ /\ / / _ \ '__|")
	print("\033[94m | || |_) \033[96m\ V / | |  __/\ V  V /  __/ |   ")
	print("\033[94m|___| .__/ \033[96m\_/  |_|\___| \_/\_/ \___|_|   ")
	print("\033[94m    |_|                     \033[93mv0.2   \033[0m")
	print("\033[93mMade by \033[96m\033[1m\033[4mhttps://github.com/ExclMark\033[0m")
	print("\033[93mDiscord: \033[96m665234248482947083")
	print("")

def main():
	clear_screen()
	logo()
	check_update()
	sleep(1)

	while True:
		query_ = query()

		if query_ == "1":
			ip = requests.get(url=f'http://api.ipify.org/').content.decode("utf-8")
			get_info(ip)
		elif query_ == "2":
			# Asking for ip
			sleep(1)
			ip = input("\033[92m\033[1mEnter ip: \033[0m")
			get_info(ip)
		elif query_ == "9":
			print("\033[94m\033[1mBye!\033[0m")
			sys.exit()
		else:
			print("\033[93mIncorrect option given.")


if __name__ == "__main__":
	main()
