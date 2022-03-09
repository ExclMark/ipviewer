import requests, sys, os
from time import sleep

def get_info():
	try:
		# Asking for ip
		sleep(1)
		ip = input("\033[92m\033[1mEnter ip: \033[0m")
		
		# Clearing terminal
		os.system("clear")
		print(f"\033[96m\033[1mChecking info about \033[94m\033[1m{ip}\033[96m\033[1m:\033[0m")

		# Requesting for ip details
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		ip = response.get("query")
		prov = response.get("isp")
		org = response.get("org")
		country = response.get("country")
		city = response.get("city")
		zip_ = response.get("zip")
		lat = response.get("lat")
		lon = response.get("lon")

		print("")
		print(f"\033[96m  > \033[0m[\033[92mCOUNTRY\033[0m]:           \033[94m\033[1m{country}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mCITY\033[0m]:              \033[94m\033[1m{city}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mZIP POSTAL CODE\033[0m]:   \033[94m\033[1m{zip_}\033[0m")
		print("")
		print(f"\033[96m  > \033[0m[\033[92mINTERNET PROVIDER\033[0m]: \033[94m\033[1m{prov}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mORGANIZATION\033[0m]:      \033[94m\033[1m{org}\033[0m")
		print("")
		print(f"\033[96m  > \033[0m[\033[92mLATITUDE\033[0m]:          \033[94m\033[1m{lat}\033[0m")
		print(f"\033[96m  > \033[0m[\033[92mLONGITUDE\033[0m]:         \033[94m\033[1m{lon}\033[0m")
		print("")
		y = input("\033[96m\033[1mView map? [y/n]: \033[0m")
		if y.lower() == "y":
			url = f"https://www.google.com/maps/search/?api=1&query={lat}%2C{lon}"
			print(f"\033[96m\033[4m{url}\n\033[0m\033[92mHold \033[4mctrl\033[0m\033[92m and click on url to open browser.")
			print("")
			sleep(1)
			print(input("\033[0mPress enter to exit... \033[0m"))
			sys.exit()
		else:
			print("\033[94m\033[1mBye!\033[0m")
			sys.exit()
	except requests.exceptions.ConnectionError:
		print("\033[93m\033[1m[!] CONNECTION ERROR!")
		print(input("Press enter to exit... "))
		sys.exit()
	except KeyboardInterrupt:
		print("\n\033[94m\033[1mBye!\033[0m")
		sys.exit()

def main():
	# Printing logo
	os.system("clear")
	print("\033[1m")
	print("\033[94m ___    \033[96m__     ___                        ")
	print("\033[94m|_ _|_ _\033[96m\ \   / (_) _____      _____ _ __ ")
	print("\033[94m | || '_ \033[96m\ \ / /| |/ _ \ \ /\ / / _ \ '__|")
	print("\033[94m | || |_) \033[96m\ V / | |  __/\ V  V /  __/ |   ")
	print("\033[94m|___| .__/ \033[96m\_/  |_|\___| \_/\_/ \___|_|   ")
	print("\033[94m    |_|                                    \033[0m")
	print("\033[93mMade by \033[96m\033[1m\033[4mhttps://github.com/ExclMark\033[0m")
	print("\033[93mDiscord: \033[96m665234248482947083")
	print("")

	get_info()

if __name__ == "__main__":
	main()
