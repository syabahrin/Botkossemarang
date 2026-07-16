import logging
import os
from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- 0. LOAD ENVIRONMENT VARIABLES ---
load_dotenv()

# --- 1. KONFIGURASI LOGGING ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- 2. DATA KOST (FULL UPDATE: NEGERI + SWASTA BARU) ---
DATA_KOST = [
    # ==========================
    # 1. KAMPUS NEGERI (DATA DARI SESI SEBELUMNYA)
    # ==========================
    
    # --- UNNES (Gunungpati) ---
    {
        "nama": "Kost Raya Tipe VVIP (UNNES)",
        "kampus": "unnes", "kategori": "negri", "jenis": "putra", "harga": 1500000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "TV", "Kulkas", "Springbed"],
        "link": "https://mamikos.com/room/kost-semarang-kost-putra-eksklusif-kost-raya-tipe-vvip-gunung-pati-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Bella (UNNES)",
        "kampus": "unnes", "kategori": "negri", "jenis": "putra", "harga": 500000,
        "fasilitas": ["Kasur", "Lemari", "Kamar Mandi Luar"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-bella-gunung-pati-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Smart 4 Kedawung (UNNES)",
        "kampus": "unnes", "kategori": "negri", "jenis": "putra", "harga": 700000,
        "fasilitas": ["Kasur", "Lemari", "WiFi", "Meja Belajar"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-smart-4-kedawung-standart-gunung-pati-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Sinta Pink Tipe A (UNNES)",
        "kampus": "unnes", "kategori": "negri", "jenis": "putri", "harga": 600000,
        "fasilitas": ["Kasur", "Lemari", "WiFi"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-sinta-pink-tipe-a-gunung-pati-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Pink (UNNES)",
        "kampus": "unnes", "kategori": "negri", "jenis": "putri", "harga": 550000,
        "fasilitas": ["Kasur", "Lemari", "Dapur Bersama"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-pink-gunung-pati-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Griya Carmel (UNNES)",
        "kampus": "unnes", "kategori": "negri", "jenis": "putri", "harga": 650000,
        "fasilitas": ["Kasur", "Lemari", "WiFi", "Parkir Motor"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-griya-carmel-gunung-pati-semarang-2?redirection_source=landing%20area"
    },

    # --- UNDIP (Tembalang) ---
    {
        "nama": "Kost Undip 19 (UNDIP)",
        "kampus": "undip", "kategori": "negri", "jenis": "putra", "harga": 750000,
        "fasilitas": ["Kasur", "Lemari", "WiFi"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-undip-19-tembalang-semarang-2?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Hijau Tipe D (UNDIP)",
        "kampus": "undip", "kategori": "negri", "jenis": "putra", "harga": 850000,
        "fasilitas": ["Kasur", "Lemari", "WiFi", "Meja Belajar"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-hijau-tipe-d-tembalang-semarang-2?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Corvettee Executive (UNDIP)",
        "kampus": "undip", "kategori": "negri", "jenis": "putra", "harga": 1800000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Water Heater", "Springbed"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-corvettee-executive-tembalang-semarang-2?redirection_source=landing%20area"
    },
    {
        "nama": "Wisma Citra Exclusive (UNDIP)",
        "kampus": "undip", "kategori": "negri", "jenis": "putri", "harga": 1600000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "TV", "Kulkas"],
        "link": "https://mamikos.com/room/kost-semarang-kost-putri-eksklusif-kost-wisma-citra-tipe-exclusive-tembalang-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Anindya (UNDIP)",
        "kampus": "undip", "kategori": "negri", "jenis": "putri", "harga": 800000,
        "fasilitas": ["Kasur", "Lemari", "WiFi", "KM Luar"],
        "link": "https://mamikos.com/room/kost-semarang-kost-putri-murah-kost-anindya-tembalang-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Hanisha Executive (UNDIP)",
        "kampus": "undip", "kategori": "negri", "jenis": "putri", "harga": 1700000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Springbed", "Akses Kartu"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-hanisha-tipe-executive-tembalang-semarang?redirection_source=landing%20area"
    },

    # --- POLINES (Banyumanik/Tembalang) ---
    {
        "nama": "Kost Wisma Genius (POLINES)",
        "kampus": "polines", "kategori": "negri", "jenis": "putra", "harga": 600000,
        "fasilitas": ["Kasur", "Lemari", "WiFi"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-wisma-genius-banyumanik-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost JN VVIP (POLINES)",
        "kampus": "polines", "kategori": "negri", "jenis": "putra", "harga": 1400000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Kloset Duduk"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-jn-vvip-banyumanik-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Putra Free Wifi (POLINES)",
        "kampus": "polines", "kategori": "negri", "jenis": "putra", "harga": 550000,
        "fasilitas": ["WiFi", "Kasur", "KM Luar"],
        "link": "https://mamikos.com/room/kost-semarang-kost-putra-murah-kost-putra-free-wifi-km-luar-area-undip-tembalang-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Marven (POLINES)",
        "kampus": "polines", "kategori": "negri", "jenis": "putri", "harga": 1300000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Springbed"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-marven-tembalang-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Anindya Tembalang (POLINES)",
        "kampus": "polines", "kategori": "negri", "jenis": "putri", "harga": 800000,
        "fasilitas": ["Kasur", "Lemari", "WiFi"],
        "link": "https://mamikos.com/room/kost-semarang-kost-putri-murah-kost-anindya-tembalang-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Jasmine Tipe B (POLINES)",
        "kampus": "polines", "kategori": "negri", "jenis": "putri", "harga": 1200000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Kloset Duduk"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-jasmine-tipe-b-tembalang-semarang-2?redirection_source=landing%20area"
    },

    # --- UIN WALISONGO (Tugu/Ngaliyan) ---
    {
        "nama": "Kost Gede Arya Tipe A (UIN)",
        "kampus": "uin walisongo", "kategori": "negri", "jenis": "putra", "harga": 500000,
        "fasilitas": ["Kasur", "Lemari", "KM Luar"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-gede-arya-tipe-a-tugu-semarang-2?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Salim (UIN)",
        "kampus": "uin walisongo", "kategori": "negri", "jenis": "putra", "harga": 1100000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Kloset Duduk"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-salim-tugu-semarang-barat?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Tanti 1 Tipe A (UIN)",
        "kampus": "uin walisongo", "kategori": "negri", "jenis": "putra", "harga": 1000000,
        "fasilitas": ["KM Dalam", "AC", "WiFi"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-tanti-1-tipe-a-tugu-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Takazi Tipe B (UIN)",
        "kampus": "uin walisongo", "kategori": "negri", "jenis": "putri", "harga": 600000,
        "fasilitas": ["Kasur", "Lemari", "WiFi", "Akses 24 Jam"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-takazi-tipe-b-ngaliyan-semarang-1?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Supriyono Tipe C (UIN)",
        "kampus": "uin walisongo", "kategori": "negri", "jenis": "putri", "harga": 550000,
        "fasilitas": ["Kasur", "Lemari", "WiFi"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-supriyono-tipe-c-ngaliyan-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Ara Tipe B (UIN)",
        "kampus": "uin walisongo", "kategori": "negri", "jenis": "putri", "harga": 650000,
        "fasilitas": ["Kasur", "Lemari", "KM Luar", "Parkir"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-ara-tipe-b-tugu-semarang-2?redirection_source=landing%20area"
    },

    # ==========================
    # 2. KAMPUS SWASTA (DATA BARU)
    # ==========================

    # --- UDINUS (Semarang Tengah) - PUTRA ---
    {
        "nama": "Kost Nurul Khaqiqoh Pavilium (UDINUS)",
        "kampus": "udinus", "kategori": "swasta", "jenis": "putra", "harga": 1500000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Springbed", "Eksklusif"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-campur-eksklusif-kost-nurul-khaqiqoh-pavilium-semarang-tengah-semarang-1?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Torisan 1 Executive (UDINUS)",
        "kampus": "udinus", "kategori": "swasta", "jenis": "putra", "harga": 1800000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "TV", "Kulkas"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-campur-eksklusif-kost-torisan-1-executive-semarang-tengah-semarang?redirection_source=landing%20area"
    },

    # --- UDINUS (Semarang Tengah) - PUTRI ---
    {
        "nama": "Kost MK (UDINUS)",
        "kampus": "udinus", "kategori": "swasta", "jenis": "putri", "harga": 650000,
        "fasilitas": ["Kasur", "Lemari", "WiFi", "Murah"],
        "link": "https://mamikos.com/room/kost-semarang-kost-putri-murah-kost-mk-semarang-tengah-1?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Nara 12 Tipe A (UDINUS)",
        "kampus": "udinus", "kategori": "swasta", "jenis": "putri", "harga": 750000,
        "fasilitas": ["Kasur", "Lemari", "WiFi", "Strategis"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-nara-12-tipe-a-semarang-tengah-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Ungu Udinus Tipe A (UDINUS)",
        "kampus": "udinus", "kategori": "swasta", "jenis": "putri", "harga": 800000,
        "fasilitas": ["Kasur", "Lemari", "Akses 24 Jam", "Dekat Kampus"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-ungu-udinus-tipe-a-semarang-tengah-semarang?redirection_source=landing%20area"
    },

    # --- UNISBANK (Semarang Selatan) - PUTRA ---
    {
        "nama": "Kost Suhardi (UNISBANK)",
        "kampus": "unisbank", "kategori": "swasta", "jenis": "putra", "harga": 500000,
        "fasilitas": ["Kasur", "Lemari", "KM Luar", "Murah"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-suhardi-semarang-selatan-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Alfahanin 05 Tipe B (UNISBANK)",
        "kampus": "unisbank", "kategori": "swasta", "jenis": "putra", "harga": 1200000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Springbed"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-alfahanin-05-tipe-b-semarang-selatan-semarang-2?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Alfahanin 05 Tipe C (UNISBANK)",
        "kampus": "unisbank", "kategori": "swasta", "jenis": "putra", "harga": 1300000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Springbed", "Luas"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-alfahanin-05-tipe-c-semarang-selatan-semarang?redirection_source=landing%20area"
    },

    # --- UNISBANK (Semarang Selatan) - PUTRI ---
    {
        "nama": "Kost V2 AC (UNISBANK)",
        "kampus": "unisbank", "kategori": "swasta", "jenis": "putri", "harga": 1400000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Kloset Duduk"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-v2-ac-semarang-tengah-semarang-2?redirection_source=landing%20area"
    },
    {
        "nama": "Kost V2 Non AC (UNISBANK)",
        "kampus": "unisbank", "kategori": "swasta", "jenis": "putri", "harga": 900000,
        "fasilitas": ["KM Dalam", "WiFi", "Kipas Angin", "Kloset Duduk"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-v2-non-ac-semarang-tengah-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Tlogo Bayem (UNISBANK)",
        "kampus": "unisbank", "kategori": "swasta", "jenis": "putri", "harga": 550000,
        "fasilitas": ["Kasur", "Lemari", "KM Luar", "Murah"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-tlogo-bayem-semarang-selatan-semarang?redirection_source=landing%20area"
    },

    # --- UNISSULA (Genuk) - PUTRA ---
    {
        "nama": "Kost Febby Genuk (UNISSULA)",
        "kampus": "unissula", "kategori": "swasta", "jenis": "putra", "harga": 500000,
        "fasilitas": ["Kasur", "Lemari", "KM Luar", "Parkir"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-febby-genuk-semarang-2?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Kahf Tipe A (UNISSULA)",
        "kampus": "unissula", "kategori": "swasta", "jenis": "putra", "harga": 1100000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Springbed"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-kahf-tipe-a-genuk-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Tasnim Tipe A (UNISSULA)",
        "kampus": "unissula", "kategori": "swasta", "jenis": "putra", "harga": 600000,
        "fasilitas": ["Kasur", "Lemari", "WiFi", "Murah"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-tasnim-tipe-a-genuk-semarang-3?redirection_source=landing%20area"
    },

    # --- UNISSULA (Genuk) - PUTRI ---
    {
        "nama": "Kost VIP Genuk (UNISSULA)",
        "kampus": "unissula", "kategori": "swasta", "jenis": "putri", "harga": 1500000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Kulkas", "VIP"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-vip-genuk-semarang?redirection_source=landing%20area"
    },
    {
        "nama": "Kost Ninaaa Genuk (UNISSULA)",
        "kampus": "unissula", "kategori": "swasta", "jenis": "putri", "harga": 600000,
        "fasilitas": ["Kasur", "Lemari", "KM Luar"],
        "link": "https://mamikos.com/room/kost-kost-putri-murah-kost-ninaaa-genuk-semarang-1?redirection_source=landing%20area"
    },
    {
        "nama": "Kost B113 Padi Raya Tipe A (UNISSULA)",
        "kampus": "unissula", "kategori": "swasta", "jenis": "putri", "harga": 700000,
        "fasilitas": ["Kasur", "Lemari", "WiFi", "Bersih"],
        "link": "https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-b113-padi-raya-tipe-a-genuk-semarang-2?redirection_source=landing%20area"
    },

    # --- USM (Arteri Soekarno Hatta) - TETAP DARI DATA SEBELUMNYA ---
    {
        "nama": "Kost Citarum Pandansari (USM)",
        "kampus": "usm", "kategori": "swasta", "jenis": "putri", "harga": 1300000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Kloset Duduk"],
        "link": "https://mamikos.com/kost/kost-dekat-usm-semarang-murah"
    },
    {
        "nama": "Kost Wisma Aruna (USM)",
        "kampus": "usm", "kategori": "swasta", "jenis": "putri", "harga": 1100000,
        "fasilitas": ["KM Dalam", "AC", "WiFi", "Kasur"],
        "link": "https://mamikos.com/kost/kost-dekat-usm-semarang-murah"
    },
    {
        "nama": "Kost Kita Jaya (USM)",
        "kampus": "usm", "kategori": "swasta", "jenis": "putra", "harga": 1100000,
        "fasilitas": ["KM Dalam", "WiFi", "AC", "Kloset Duduk"],
        "link": "https://mamikos.com/kost/kost-dekat-usm-semarang-murah"
    },
]

# --- 3. BOBOT KRITERIA SAW ---
W_HARGA = 0.6
W_FASILITAS = 0.4

# --- 4. LOGIKA PERHITUNGAN SAW ---
def hitung_saw_filter(kampus_pilihan, jenis_kelamin):
    kandidat = [
        k for k in DATA_KOST 
        if k['kampus'] == kampus_pilihan and k['jenis'] == jenis_kelamin
    ]
    
    if not kandidat:
        return []

    hasil_akhir = []
    
    # Hitung Skor Fasilitas
    for k in kandidat:
        k['skor_fasilitas_angka'] = len(k['fasilitas'])

    # Mencari Min/Max
    list_harga = [k['harga'] for k in kandidat]
    list_skor_fasilitas = [k['skor_fasilitas_angka'] for k in kandidat]

    min_harga = min(list_harga)
    max_fasilitas = max(list_skor_fasilitas)

    # Perhitungan SAW
    for k in kandidat:
        norm_harga = min_harga / k['harga']
        
        if max_fasilitas == 0:
            norm_fasilitas = 0
        else:
            norm_fasilitas = k['skor_fasilitas_angka'] / max_fasilitas
        
        nilai_akhir = (norm_harga * W_HARGA) + (norm_fasilitas * W_FASILITAS)
        
        k_hasil = k.copy()
        k_hasil['skor_saw'] = nilai_akhir
        hasil_akhir.append(k_hasil)
    
    hasil_akhir.sort(key=lambda x: x['skor_saw'], reverse=True)
    return hasil_akhir

# --- 5. BOT HANDLERS ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    keyboard = [["👨 Kos Putra", "👩 Kos Putri"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text(
        "Halo! Selamat datang di Bot SPK Kos.\nSilakan pilih jenis kos yang dicari:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_data = context.user_data
    
    # TAHAP 1: GENDER
    if text == "👨 Kos Putra" or text == "👩 Kos Putri":
        if "Putra" in text:
            user_data['jenis_pilihan'] = 'putra'
            label = "Putra"
        else:
            user_data['jenis_pilihan'] = 'putri'
            label = "Putri"
            
        keyboard_kategori = [["🏛 Kampus Negeri", "🏢 Kampus Swasta"]]
        reply_markup = ReplyKeyboardMarkup(keyboard_kategori, resize_keyboard=True, one_time_keyboard=True)
        
        await update.message.reply_text(
            f"Oke, mencari Kos **{label}**.\nSelanjutnya, pilih kategori kampusnya:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        return

    # TAHAP 2: KATEGORI KAMPUS
    if text == "🏛 Kampus Negeri" or text == "🏢 Kampus Swasta":
        if 'jenis_pilihan' not in user_data:
            await update.message.reply_text("⚠️ Ulangi dari awal ketik /start")
            return

        if text == "🏛 Kampus Negeri":
            keyboard_kampus = [["UNNES", "UNDIP"], ["POLINES", "UIN Walisongo"]]
        else:
            keyboard_kampus = [["UDINUS", "USM"], ["UNISBANK", "UNISSULA"]]
            
        reply_markup = ReplyKeyboardMarkup(keyboard_kampus, resize_keyboard=True, one_time_keyboard=True)
        await update.message.reply_text(
            f"Silakan pilih kampus spesifik di bawah ini:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        return

    # TAHAP 3: EKSEKUSI (Berdasarkan Nama Kampus)
    kampus_code = text.lower()
    daftar_kampus_valid = ["unnes", "undip", "polines", "uin walisongo", "udinus", "usm", "unisbank", "unissula"]
    
    if kampus_code not in daftar_kampus_valid:
        await update.message.reply_text("⚠️ Tombol tidak dikenali. Gunakan tombol yang tersedia.")
        return

    if 'jenis_pilihan' not in user_data:
        await update.message.reply_text("⚠️ Sesi habis, ketik /start lagi.")
        return
        
    jenis_dipilih = user_data['jenis_pilihan']

    await update.message.reply_text(f"🔍 Mencari Kos {jenis_dipilih.capitalize()} di area kampus {text}...")
    rekomendasi = hitung_saw_filter(kampus_code, jenis_dipilih)
    
    if not rekomendasi:
        await update.message.reply_text(f"Maaf, belum ada data untuk kampus {text} di database kami.")
        return

    # TAMPILKAN HASIL DENGAN LINK
    pesan = f"🏆 **REKOMENDASI KOS DI {text.upper()}** 🏆\n"
    pesan += f"Kategori: Kos {jenis_dipilih.capitalize()}\n\n"
    
    for i, kos in enumerate(rekomendasi, 1):
        str_fasilitas = ", ".join(kos['fasilitas'])
        
        # Format Pesan dengan Hyperlink Telegram: [Teks](URL)
        pesan += (
            f"{i}. **[{kos['nama']}]({kos['link']})**\n" # <--- Nama Kos jadi Link Biru
            f"   ⭐ Skor SAW: {kos['skor_saw']:.3f}\n"
            f"   💰 Harga: Rp {kos['harga']:,}\n"
            f"   🛠 **Fasilitas:** {str_fasilitas}\n"
            f"   🔗 [Lihat Detail & Foto]({kos['link']})\n"
            f"   ------------------------\n"
        )
        
    await update.message.reply_text(pesan, parse_mode='Markdown', disable_web_page_preview=True)

# --- 6. MAIN PROGRAM ---
if __name__ == '__main__':
    TOKEN = os.getenv('BOT_TOKEN') 
    
    if not TOKEN:
        print("❌ Token tidak ditemukan di file .env")
    else:
        print("✅ Bot Berjalan dengan Link Mamikos...")
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        app.run_polling()