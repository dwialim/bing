# ⚡ Fitur
- Multi-akun dengan user data dir tersimpan
- Viewport per akun atau random untuk menghindari deteksi
- Random query generation
- Tampilan terminal berwarna (colorama)
- Konfigurasi akun dan viewport via `.env`

---

## 🛠 Prasyarat Linux
- Python 3.10+
- Node.js
- Playwright browser (Chromium)

---

## 🛠 Prasyarat Mac 12
- Selenium
- Chrome/Firefox

---

## 📦 Instalasi Package for Linux
1. Install Python package dependencies:
	```sh
	pip install playwright python-dotenv colorama
	```
2. Install browser yang dibutuhkan oleh Playwright:
	```sh
	playwright install
	```
	>Catatan: Pastikan chromium terinstall melalui perintah di atas.

---

## 📦 Instalasi Package for Mac 12
1.  Install dependencies di macOS 12:
	```sh
	pip install selenium webdriver-manager python-dotenv colorama
	brew install --cask chromedriver
	```
	>Jika pakai Firefox, install geckodriver juga:
	```sh
	brew install geckodriver
	```

---

## 🔑 Konfigurasi .env
Buat file .env di folder yang sama dengan script:
```sh
# Akun format: email:path_user_data_dir (bisa > 1, pisahkan dengan koma)
ACCOUNTS=account1@gmail.com:~/.bingbot/account1@gmail.com,account2@gmail.com:~/.bingbot/account2@gmail.com

# Viewport format: email:widthxheight (optional) bisa > 1 pisahkan dengan koma
VIEWPORTS=account1@gmail.com:1600x900


# Default value for oppo reno 11F (sesuaikan dengan tombol backspace pada HP)
# semakin besar value, arahnya semakin ke kanan
BACKSPACE_X=950
# semakin besar value, arahnya semakin ke bawah
BACKSPACE_Y=2100
```
>Kamu bisa menambahkan akun baru dengan format yang sama. Jika akun tidak ada di VIEWPORTS, bot akan generate ukuran random.


---


## 🔨 Menjalankan Bot
1. Jalankan script:
	```sh
	python auto_search.py
	```
	> untuk Linux
	```sh
	python macos.py
	```
	> untuk Linux
2. Pilih akun dengan nomor (default `1` jika tekan Enter).
3. Tunggu hitung mundur 3 detik, bot akan mulai melakukan pencarian.


---

## ⚙️ Alur Kerja Bot
```pgsql
		  ┌───────────────┐
		  │ Load .env     │
		  │ ACCOUNTS &    │
		  │ VIEWPORTS     │
		  └───────┬───────┘
				  │
				  ▼
		┌───────────────────┐
		│ Pilih akun oleh   │
		│ user (input)      │
		└─────────┬─────────┘
				  │
				  ▼
	   ┌─────────────────────┐
	   │ Ambil user_data_dir │
	   │ & viewport akun     │
	   └──────────┬──────────┘
				  │
				  ▼
	┌───────────────────────────┐
	│ Launch Chromium dengan    │
	│ persistent context        │
	│ (user_data_dir & viewport)│
	└─────────────┬─────────────┘
				  │
				  ▼
		┌────────────────────┐
		│ Loop setiap query  │
		│ - Buka Bing        │
		│ - Isi search box   │
		│ - Tekan Enter      │
		│ - Tunggu random    │
		└─────────┬──────────┘
				  │
				  ▼
		   ┌──────────────┐
		   │ Selesai semua│
		   │ query        │
		   └──────────────┘

```

---

## 📝 Catatan
- Gunakan `headless=False` agar jendela Chromium terlihat dan mudah debugging (Linux).
- Jangan jalankan terlalu cepat agar tidak terdeteksi bot oleh Bing.
- `user_data_dir` unik per akun agar sesi tidak tercampur.


---


## 🔧 Tips
- Tambah akun baru: edit `.env` `ACCOUNTS` dan `VIEWPORTS`.
- Ubah jumlah query: edit `range(35)` di script.
- Viewport random otomatis jika akun tidak ada di `.env`.
