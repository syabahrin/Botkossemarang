import mysql.connector
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, ContextTypes

# Menentukan tahapan (state) percakapan
GENDER, KATEGORI, KAMPUS = range(3)

# ==========================================
# 1. FUNGSI DATABASE (UPDATE PERHITUNGAN FASILITAS TEKS)
# ==========================================
def dapatkan_rekomendasi_saw(gender_pilihan, kampus_pilihan):
    koneksi = None
    try:
        koneksi = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="rekomendasi_kos"
        )
        cursor = koneksi.cursor(dictionary=True)
        query = "SELECT * FROM indekos WHERE gender = %s AND nama_kampus = %s"
        cursor.execute(query, (gender_pilihan, kampus_pilihan))
        daftar_kos = cursor.fetchall()

        if not daftar_kos:
            return [] 

        # Mengambil nilai Harga (Sudah Angka)
        list_harga = [kos['harga'] for kos in daftar_kos]
        
        # MENGHITUNG TEKS FASILITAS MENJADI ANGKA
        # Teks "Kasur, Lemari, WiFi" akan dihitung otomatis oleh Python menjadi angka 3
        list_fasilitas_angka = [len(kos['fasilitas'].split(',')) for kos in daftar_kos]
        
        min_harga = min(list_harga)
        max_fasilitas = max(list_fasilitas_angka) # Max dari angka fasilitas
        
        w1, w2 = 0.6, 0.4 

        hasil_perankingan = []
        for kos in daftar_kos:
            # Normalisasi Harga (Cost)
            r1 = min_harga / kos['harga']
            
            # Normalisasi Fasilitas (Benefit) dengan mengubah teks jadi angka dulu
            jumlah_fasilitas = len(kos['fasilitas'].split(','))
            r2 = jumlah_fasilitas / max_fasilitas
            
            # Nilai Preferensi V
            nilai_v = (w1 * r1) + (w2 * r2)
            
            hasil_perankingan.append({
                'nama_kos': kos['nama_kos'],
                'harga': kos['harga'],
                'fasilitas': kos['fasilitas'], # Tetap menyimpan teks aslinya untuk ditampilkan
                'skor_v': round(nilai_v, 3),
                'link': kos['link_mamikos']
            })

        hasil_perankingan.sort(key=lambda x: x['skor_v'], reverse=True)
        return hasil_perankingan

    except mysql.connector.Error as err:
        print(f"Error Database: {err}")
        return None
    finally:
        if koneksi and koneksi.is_connected():
            cursor.close()
            koneksi.close() 

# ==========================================
# 2. ALUR PERCAKAPAN BOT TELEGRAM (UPDATE HTML)
# ==========================================

async def mulai(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [
        [
            InlineKeyboardButton("👨 Kos Putra", callback_data='Putra'),
            InlineKeyboardButton("👩 Kos Putri", callback_data='Putri')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Halo! Selamat datang di Bot Rekomendasi Indekos Semarang. 🏠\n\n"
        "Silakan <b>KLIK</b> jenis kos yang Anda cari di bawah ini:",
        reply_markup=reply_markup,
        parse_mode='HTML' # Mengubah ke HTML
    )
    return GENDER

async def pilih_gender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer() 
    
    context.user_data['gender'] = query.data
    
    keyboard = [
        [
            InlineKeyboardButton("🏛️ Kampus Negeri", callback_data='Negeri'),
            InlineKeyboardButton("🏢 Kampus Swasta", callback_data='Swasta')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text=f"Baik, Anda mencari Kos {query.data}.\nSekarang, <b>KLIK</b> kategori kampus Anda:",
        reply_markup=reply_markup,
        parse_mode='HTML' # Mengubah ke HTML
    )
    return KATEGORI

async def pilih_kategori(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    kategori = query.data
    
    if kategori == 'Negeri':
        keyboard = [
            [InlineKeyboardButton("UNNES", callback_data='UNNES'), InlineKeyboardButton("UNDIP", callback_data='UNDIP')],
            [InlineKeyboardButton("POLINES", callback_data='POLINES'), InlineKeyboardButton("UIN Walisongo", callback_data='UIN Walisongo')]
        ]
    else:
        keyboard = [
            [InlineKeyboardButton("UDINUS", callback_data='UDINUS'), InlineKeyboardButton("USM", callback_data='USM')],
            [InlineKeyboardButton("UNISBANK", callback_data='UNISBANK'), InlineKeyboardButton("UNISSULA", callback_data='UNISSULA')]
        ]
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text="Satu langkah lagi! <b>KLIK</b> nama kampus Anda:",
        reply_markup=reply_markup,
        parse_mode='HTML' # Mengubah ke HTML
    )
    return KAMPUS

async def pilih_kampus_dan_hitung(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    kampus_pilihan = query.data
    gender_pilihan = context.user_data['gender']
    
    await query.edit_message_text(
        text=f"🔍 Sedang menghitung rumus SAW untuk rekomendasi di sekitar <b>{kampus_pilihan}</b>...",
        parse_mode='HTML' # Mengubah ke HTML
    )
    
    hasil = dapatkan_rekomendasi_saw(gender_pilihan, kampus_pilihan)
    
    if hasil is None:
        teks_balasan = "Maaf, terjadi kesalahan pada database MySQL Anda."
    elif len(hasil) == 0:
        teks_balasan = f"Maaf, belum ada data di database untuk Kos {gender_pilihan} di sekitar {kampus_pilihan}."
    else:
        teks_balasan = f"🏆 <b>REKOMENDASI KOS TERBAIK (SAW)</b> 🏆\nKriteria: Kos {gender_pilihan} | Lokasi: {kampus_pilihan}\n\n"
        for urutan, kos in enumerate(hasil[:3], start=1):
           teks_balasan += (
                f"<b>{urutan}. {kos['nama_kos']}</b>\n"
                f"↳ Skor SAW : {kos['skor_v']}\n"
                f"↳ Harga    : Rp{kos['harga']:,}\n"
                f"↳ Fasilitas: {kos['fasilitas']}\n" # <--- Berubah di baris ini
                f"↳ Link     : <a href='{kos['link']}'>Buka di Mamikos</a>\n\n"
            )
            
    await context.bot.send_message(chat_id=update.effective_chat.id, text=teks_balasan, parse_mode='HTML')
    
    return ConversationHandler.END

# ==========================================
# 3. FUNGSI UTAMA (MAIN)
# ==========================================
def main():
    # MASUKKAN TOKEN BOT TELEGRAM ANDA DI SINI
    TOKEN_BOT = ""
    
    application = Application.builder().token(TOKEN_BOT).build()

    # Perhatikan perubahannya di sini: Kita pakai CallbackQueryHandler, bukan MessageHandler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', mulai)],
        states={
            GENDER: [CallbackQueryHandler(pilih_gender)],
            KATEGORI: [CallbackQueryHandler(pilih_kategori)],
            KAMPUS: [CallbackQueryHandler(pilih_kampus_dan_hitung)],
        },
        fallbacks=[CommandHandler('start', mulai)]
    )

    application.add_handler(conv_handler)

    print("Bot sedang berjalan... Tekan Ctrl+C di terminal untuk menghentikan.")
    application.run_polling()

if __name__ == '__main__':
    main()
