import time

meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SUS": "Tanggapan Untuk Sesuatu Mencurigakan",
            "NOOB": "Ejekan Untuk Pemain Amatir",
            "RATIO": "Ejekan Untuk Orang Yang memiliki komentar banyak daripada like",
            "GTG": "Bahasa Inggrisnya: Go To Go, Yang artinya Harus Pergi",
            "AMOGUS": "Kata Aslinya Among Us, Tapi Di Plesetkan Untuk Kelucuan"
            }
            
        
        
        
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua agar kami bisa mengetahui kata tersebut:): ")

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print("Mencari...")
    time.sleep(3)
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("Mencari...")
    time.sleep(3)
    print("KATA TERSEBUT TIDAK ADA DI LIST INI ATAU KATA TERSEBUT TIDAK PANTAS")
