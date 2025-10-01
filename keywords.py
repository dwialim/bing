keyword = [
	# 🌐 Teknologi & Komputer
	"Python", "Machine learning", "Artificial intelligence", "Web development",
	"Data science", "Linux", "Automation", "Edge browser", "Programming",
	"Open source", "Cloud computing", "Cybersecurity", "IoT", "Big data",
	"DevOps", "GitHub", "Docker", "Kubernetes", "JavaScript", "React",
	"Node.js", "API", "Database", "SQL", "NoSQL", "Blockchain", "Cryptocurrency",
	"Robotics", "Testing", "UI/UX", "Agile", "Scrum", "Networking", "5G",
	"Mobile development", "Java", "Go", "Rust", "TypeScript", "HTML", "CSS",

	# 📰 Berita & Tren
	"Pemilu 2025", "Harga emas hari ini", "Berita teknologi terbaru",
	"Tren startup Indonesia", "Ekonomi global", "Harga saham Tesla",
	"Perang dagang AS China", "Update sepak bola", "Liga Champions",
	"Transfer pemain terbaru", "Piala Dunia", "Berita cuaca", "Banjir Jakarta",
	"Gempa terbaru", "Isu lingkungan", "Kebijakan pemerintah",

	# 🏠 Lifestyle & Hobi
	"Resep masakan sederhana", "Kopi susu kekinian", "Review smartphone terbaru",
	"Laptop terbaik untuk mahasiswa", "Travel Bali murah", "Destinasi wisata Jepang",
	"Hotel murah Bandung", "Tempat nongkrong Jakarta", "Cafe hits Surabaya",
	"Ide dekorasi rumah", "Desain kamar minimalis", "Tren fashion 2025",
	"Skincare routine", "Tips kesehatan", "Olahraga di rumah", "Fitness tips",
	"Nutrisi seimbang", "Yoga untuk pemula", "Meditasi singkat", "Manajemen waktu",
	"Cara investasi", "Tabungan anak muda", "Crypto terbaru", "Saham blue chip",

	# 🎬 Hiburan
	"Film bioskop terbaru", "Drama Korea populer", "Netflix rekomendasi",
	"Anime terbaik", "Musik trending", "Lagu populer 2025", "Konser Coldplay",
	"Game online terbaru", "Tips Mobile Legends", "Genshin Impact update",
	"PS5 review", "Nintendo Switch game", "Film Marvel terbaru",

	# 📚 Pendidikan & Pengetahuan
	"Sejarah Indonesia", "Filsafat dasar", "Psikologi populer", "Belajar bahasa Inggris",
	"Tips TOEFL", "Belajar bahasa Jepang", "Belajar coding online", "Kursus gratis",
	"Astronomi", "Penjelajahan luar angkasa", "Sains populer", "Inovasi teknologi",
	"Perubahan iklim", "Sustainability", "Startup inovatif"
]
android = [
    # Teknologi
    "python", "docker", "kubernetes", "linux", "android", "ios", "ai", "chatgpt",
    "cloud", "aws", "gcp", "azure", "devops", "cyber", "5g", "vr", "ar", "robot",
    # Berita & Tren
    "politik", "ekonomi", "cuaca", "gempa", "banjir", "inflasi", "crypto", "bitcoin",
    "elon musk", "tesla", "nvidia", "meta", "apple", "google", "microsoft",
    # Hiburan
    "musik", "film", "drakor", "anime", "manga", "kpop", "spotify", "netflix",
    "tiktok", "youtube", "instagram", "twitter", "facebook",
    # Olahraga
    "fifa", "nba", "messi", "ronaldo", "badminton", "voli", "tenis", "formula 1",
    # Keuangan
    "dollar", "rupiah", "emas", "saham", "trading", "investasi", "obligasi",
    # Lain-lain / Random
    "makanan", "kopi", "teh", "game", "mobile", "pubg", "valorant", "minecraft",
    "travel", "jakarta", "bandung", "bali", "jepang", "korea", "singapura",
]

import random

# Fungsi untuk membuat query pencarian panjang dengan menggabungkan beberapa kata kunci
def generate_long_query():
	num_keywords = random.randint(2, 5)  # Ambil 2 sampai 5 kata kunci
	selected_keywords = random.sample(keyword, num_keywords)
	return " ".join(selected_keywords)

def generate_query_android():
	num_keywords = random.randint(2, 4)  # Ambil 2 sampai 5 kata kunci
	selected_keywords = random.sample(android, num_keywords)
	return " ".join(selected_keywords)
