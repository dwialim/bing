#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from playwright.sync_api import sync_playwright
import time, random, os
from keywords import generate_long_query
from colorama import Fore, Style, init
from dotenv import load_dotenv

init(autoreset=True)  # supaya warna reset otomatis

load_dotenv()  # load .env

# 📂 Lokasi folder user_data_dir untuk masing-masing akun
ACCOUNTS = {}
for item in os.getenv("ACCOUNTS", "").split(","):
	if ":" in item:
		email, path = item.split(":")
		ACCOUNTS[email] = os.path.expanduser(path)

# 🎛 Viewport per akun (optional)
VIEWPORTS = {}
for item in os.getenv("VIEWPORTS", "").split(","):
	if ":" in item:
		email, size = item.split(":")
		width, height = map(int, size.split("x"))
		VIEWPORTS[email] = {"width": width, "height": height}

# 🔑 Generate query random
keywords = [generate_long_query() for _ in range(35)]

def search_with_profile(playwright, profile_dir, account_name):
	# ambil viewport akun, kalau tidak ada buat random
	viewport = VIEWPORTS.get(account_name) or {
		"width": random.randint(1200, 1920),
		"height": random.randint(700, 1080)
	}

	context = playwright.chromium.launch_persistent_context(
		user_data_dir=profile_dir,
		headless=False,
		# args=["--start-maximized"]
		args=[f"--window-size={viewport['width']},{viewport['height']}"],
		viewport=viewport
		# args=["--window-size=1920,1080"],  # <-- set ukuran jendela secara manual
		# viewport={"width": 1920, "height": 1080}  # <-- set viewport Playwright
	)
	page = context.new_page()

	print(Fore.CYAN + f"\n🌐 Membuka Bing untuk akun: {account_name}")
	# buka homepage dulu
	page.goto("https://www.bing.com")
	time.sleep(random.uniform(2, 5))

	try:
		for i, q in enumerate(keywords, 1):
			print(Fore.YELLOW + f"[{i}/{len(keywords)}] ({account_name}) Searching: {q}")

			search_box = page.locator("textarea[name='q'], input[name='q']").first
			search_box.fill("")

			search_box.press_sequentially(q, delay=50)

			time.sleep(random.uniform(0.5, 1.5))
			search_box.press("Enter")

			time.sleep(random.uniform(5, 15))

		print(Fore.GREEN + f"\n✅ Selesai dengan akun: {account_name}")

	except KeyboardInterrupt:
		print(Fore.RED + "\n🛑 Stopped by user (Ctrl+C)" + Style.RESET_ALL)


if __name__ == "__main__":
	print(Fore.MAGENTA + "=" * 50)
	print(Fore.CYAN + "      🔎 Bing Auto Search Bot (Playwright)")
	print(Fore.MAGENTA + "=" * 50)

	# tampilkan pilihan akun
	print("\nPilih akun:")
	for idx, name in enumerate(ACCOUNTS.keys(), start=1):
		print(Fore.YELLOW + f"[{idx}] {name}")

	choice = input(Fore.CYAN + "Masukkan nomor akun (default=1): ").strip()

	# default pilih akun pertama kalau user tekan Enter
	if choice == "":
		choice_idx = 1
	else:
		try:
			choice_idx = int(choice)
		except ValueError:
			print(Fore.RED + "❌ Input tidak valid.")
			exit(1)

	try:
		account = list(ACCOUNTS.keys())[choice_idx - 1]
	except (ValueError, IndexError):
		print(Fore.RED + "❌ Nomor akun tidak tersedia.")
		exit(1)

	profile_dir = ACCOUNTS[account]
	os.makedirs(profile_dir, exist_ok=True)

	print(Fore.CYAN + f"\n➡️  Akun yang dipilih: {Fore.GREEN}{account}")
	print(Fore.CYAN + f"➡️  Total pencarian: {Fore.GREEN}{len(keywords)} queries")

	# Hitung mundur sebelum mulai
	print(Fore.MAGENTA + "\n⏳ Mulai dalam:")
	for sec in range(3, 0, -1):
		print(Fore.YELLOW + f"{sec}...", end=" ", flush=True)
		time.sleep(1)
	print(Fore.GREEN + "GO!\n")

	with sync_playwright() as p:
		search_with_profile(p, profile_dir, account)
