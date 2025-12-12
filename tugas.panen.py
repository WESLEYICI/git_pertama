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

#tugas soal no.2
print("Jagung lokasi2:", data_panen['lokasi2']['hasil_panen']['jagung'])


#tugas soal no.3
print("Nama lokasi3:", data_panen['lokasi3']['nama_lokasi'])


#tugas soal no.4
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

print("Variabel padi dan kedelai setiap lokasi berhasil dibuat.")


