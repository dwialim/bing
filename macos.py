#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, random, os
from keywords import generate_long_query
from colorama import Fore, init
from dotenv import load_dotenv

init(autoreset=True)
load_dotenv()

# 📂 Lokasi folder user_data_dir untuk tiap akun
ACCOUNTS = {}
for item in os.getenv("ACCOUNTS", "").split(","):
	if ":" in item:
		email, path = item.split(":")
		ACCOUNTS[email] = os.path.expanduser(path)

# 🔑 Generate query random
keywords = [generate_long_query() for _ in range(35)]

def search_with_selenium(account_name):
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

	print(Fore.CYAN + f"\n🌐 Membuka Bing untuk akun: {account_name}")
	driver.get("https://www.bing.com")
	time.sleep(random.uniform(2, 5))

	try:
		for i, q in enumerate(keywords, 1):
			print(Fore.YELLOW + f"[{i}/{len(keywords)}] ({account_name}) Searching: {q}")
			search_box = driver.find_element(By.NAME, "q")
			search_box.clear()
			search_box.send_keys(q)
			search_box.send_keys(Keys.ENTER)
			time.sleep(random.uniform(5, 15))

		print(Fore.GREEN + f"\n✅ Selesai dengan akun: {account_name}")
	except KeyboardInterrupt:
		print(Fore.RED + "\n🛑 Stopped by user (Ctrl+C)")
	finally:
		driver.quit()

if __name__ == "__main__":
	print(Fore.MAGENTA + "="*50)
	print(Fore.CYAN + "      🔎 Bing Auto Search Bot (Selenium)")
	print(Fore.MAGENTA + "="*50)

	# pilih akun
	print("\nPilih akun:")
	for idx, name in enumerate(ACCOUNTS.keys(), start=1):
		print(Fore.YELLOW + f"[{idx}] {name}")

	choice = input(Fore.CYAN + "Masukkan nomor akun (default=1): ").strip()
	choice_idx = int(choice) if choice else 1
	account = list(ACCOUNTS.keys())[choice_idx - 1]

	print(Fore.CYAN + f"\n➡️  Akun yang dipilih: {Fore.GREEN}{account}")
	print(Fore.CYAN + f"➡️  Total pencarian: {Fore.GREEN}{len(keywords)} queries")

	search_with_selenium(account)
