'''
Buatlah dua kelas Persegi dan Lingkaran dengan metode hitungLuas(). Gunakan konsep
polimorfisme agar kita dapat menghitung luas dari objek berbentuk persegi atau lingkaran
tanpa memeriksa jenis objek secara eksplisit.
Contoh output:
persegi = Persegi(5)
lingkaran = Lingkaran(3)
print(f"Luas Persegi: {persegi.hitungLuas()}") # Output: Luas Persegi: 25
print(f"Luas Lingkaran: {lingkaran.hitungLuas()}") # Output: Luas Lingkaran:
28.274333882308138
'''

class BangunDatar:
    def hitungLuas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(BangunDatar):
    def __init__(self, jariJari):
        self.jariJari = jariJari

    def hitungLuas(self):
        return 3.14 * self.jariJari ** 2

#input dan output yang muncul
persegi = Persegi(5)
lingkaran = Lingkaran(3)

print(f"Luas Persegi: {persegi.hitungLuas()}")         # Output: Luas Persegi: 25
print(f"Luas Lingkaran: {lingkaran.hitungLuas()}")     # Output: Luas Lingkaran: 28.27433
'''
Output yang muncul untuk luas lingkaran = 28.26
Jika menggunakan 22/7, maka output luas lingkaran = 28.285714285714285
Untuk memunculkan output sesuai dengan contoh,
phi yang digunakan adalah 3.1415923
'''