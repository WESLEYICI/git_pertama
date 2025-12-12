data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panenn': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panenn': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panenn': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panenn': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panenn': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# -----------------------------
# SOAL NO.2
# -----------------------------
print("Jagung lokasi2:", data_panen['lokasi2']['hasil_panenn']['jagung'])

# -----------------------------
# SOAL NO.3
# -----------------------------
print("Nama lokasi3:", data_panen['lokasi3']['nama_lokasi'])

# -----------------------------
# SOAL NO.4
# -----------------------------
padi_lokasi1 = data_panen['lokasi1']['hasil_panenn']['padi']
kedelai_lokasi1 = data_panen['lokasi1']['hasil_panenn']['kedelai']

padi_lokasi2 = data_panen['lokasi2']['hasil_panenn']['padi']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panenn']['kedelai']

padi_lokasi3 = data_panen['lokasi3']['hasil_panenn']['padi']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panenn']['kedelai']

padi_lokasi4 = data_panen['lokasi4']['hasil_panenn']['padi']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panenn']['kedelai']

padi_lokasi5 = data_panen['lokasi5']['hasil_panenn']['padi']
kedelai_lokasi5 = data_panen['lokasi5']['hasil_panenn']['kedelai']

print("Soal No.4 selesai: variabel padi & kedelai tiap lokasi dibuat.")

# -----------------------------
# SOAL NO.5
# -----------------------------
padi_semua_lokasi = [
    padi_lokasi1, padi_lokasi2, padi_lokasi3, padi_lokasi4, padi_lokasi5
]

kedelai_semua_lokasi = [
    kedelai_lokasi1, kedelai_lokasi2, kedelai_lokasi3, kedelai_lokasi4, kedelai_lokasi5
]

print("Soal No.5 selesai: variabel daftar padi & kedelai semua lokasi dibuat.")

# -----------------------------
# SOAL NO.6
# -----------------------------
print("\nSoal No.6: Mengecek lokasi yang memerlukan perhatian khusus:\n")

for lokasi, info in data_panen.items():
    padi = info['hasil_panenn']['padi']
    jagung = info['hasil_panenn']['jagung']
    nama = info['nama_lokasi']

    if padi > 1300 or jagung > 800:
        print(f"{nama} ({lokasi}) memerlukan perhatian khusus!")
    else:
        print(f"{nama} ({lokasi}) dalam kondisi normal.")
