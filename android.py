# Latest
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import logging
from keywords import generate_query_android
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from dotenv import load_dotenv


# ==========================
# Konfigurasi
# ==========================
BING_PACKAGE = "com.microsoft.bing"
BING_ACTIVITY = "com.microsoft.sapphire.app.main.SapphireMainActivity"

QUERIES = [generate_query_android() for _ in range(20)]

# Default value for oppo reno 11F
BACKSPACE_X = os.getenv("BACKSPACE_X", "950") # semakin besar value, arahnya semakin ke kanan
BACKSPACE_Y = os.getenv("BACKSPACE_Y", "2100") # semakin besar value, arahnya semakin ke bawah

LOG_FILE = "bing_autosearch.log"

# Posisi search box (tap coordinates), sesuaikan dengan device
SEARCH_BOX_X = 300
SEARCH_BOX_Y = 200

# ==========================
# Setup logging
# ==========================
logging.basicConfig(
	filename=LOG_FILE,
	level=logging.INFO,
	format="%(asctime)s - %(levelname)s - %(message)s",
)

# ==========================
# Appium Setup
# ==========================
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Device"
options.app_package = BING_PACKAGE
options.app_activity = BING_ACTIVITY
options.automation_name = "UiAutomator2"
options.no_reset = True
options.new_command_timeout = 300

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(5)

# ==========================
# Helper Functions
# ==========================
def tap_search_box():
	"""Tap di posisi search box agar fokus"""
	driver.tap([(SEARCH_BOX_X, SEARCH_BOX_Y)], 100)
	time.sleep(random.uniform(0.5, 1.0))

def input_query(query):
	"""Ketik query dan tekan enter"""
	clear_search_box()
	for ch in query:
		driver.press_keycode(char_to_keycode(ch))
		time.sleep(random.uniform(0.01, 0.02))
	driver.press_keycode(66)  # Enter
	time.sleep(random.uniform(2, 10))

def clear_search_box(length=50):
	# """
	# Clear search box dengan menekan backspace.
	# length: jumlah backspace yang ditekan, default 50 (cukup untuk sebagian besar query)
	# """
	# for _ in range(length):
	# 	driver.press_keycode(67)  # 67 = KEYCODE_DEL (Backspace)
	# 	time.sleep(random.uniform(0.01, 0.02))
	"""Tahan tombol backspace selama 10 detik untuk menghapus isi kotak pencarian"""
	try:
		logging.info("Menahan tombol backspace selama 5 detik (pakai W3C Actions)...")

		finger = PointerInput("touch", "finger")
		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=finger)

		actions.w3c_actions.pointer_action.move_to_location(BACKSPACE_X, BACKSPACE_Y)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(5)  # tahan 10 detik
		actions.w3c_actions.pointer_action.pointer_up()
		actions.perform()

		time.sleep(0.5)
	except Exception as e:
		logging.warning(f"Gagal long press backspace: {e}")

def char_to_keycode(ch):
	"""Map karakter ke keycode Android (hanya huruf kecil & spasi)"""
	key_map = {
		# huruf
		"a":29,"b":30,"c":31,"d":32,"e":33,"f":34,"g":35,"h":36,"i":37,
		"j":38,"k":39,"l":40,"m":41,"n":42,"o":43,"p":44,"q":45,"r":46,
		"s":47,"t":48,"u":49,"v":50,"w":51,"x":52,"y":53,"z":54,
		# angka
		"0":7,"1":8,"2":9,"3":10,"4":11,"5":12,"6":13,"7":14,"8":15,"9":16,
		# spasi
		" ":62
	}
	return key_map.get(ch.lower(), 62)  # default spasi

def scroll_results():
	# """Scroll hasil search beberapa kali"""
	# for _ in range(random.randint(2,5)):
	# 	driver.swipe(500, 1500, 500, 500, 500)
	# 	time.sleep(random.uniform(0.5, 1.0))
	"""Scroll hasil search dengan pola acak"""
	num_scrolls = random.randint(0, 5)
	logging.info(f"Scrolling {num_scrolls}x dengan variasi acak")

	for i in range(num_scrolls):
		# posisi awal & akhir scroll dibuat acak
		start_x = random.randint(400, 600)
		start_y = random.randint(1300, 1700)
		end_y   = random.randint(400, 700)
		duration = random.randint(400, 800)  # milidetik

		driver.swipe(start_x, start_y, start_x, end_y, duration)

		# jeda acak antar scroll
		delay = random.uniform(0.4, 1.2)
		time.sleep(delay)

def search_query(query):
	logging.info(f"Searching: {query}")
	tap_search_box()
	input_query(query)
	scroll_results()

# ==========================
# Main
# ==========================
for q in QUERIES:
	search_query(q)
	time.sleep(random.randint(2,5))

driver.quit()
logging.info("All queries processed.")
