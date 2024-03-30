'''
Buatlah kelas induk Hewan dengan atribut nama dan jenis kelamin metode bersuara(),
makan(), dan minum(). Kemudian buat dua kelas anak (turunannya) Kucing dan Anjing
yang mewarisi metode dari kelas Hewan. Metode menghasilkan masing-masing output
yang berbeda.
Contoh output:
hewan1 = Kucing("Kiki", “Betina”)
hewan2 = Anjing("Ichi", “Jantan”)
print(hewan1.nama) # Output: Kiki
print(hewan2.nama) # Output: Ichi
hewan1.bersuara() # Output: Kucing Kiki bersuara: Meong!
hewan1.bersuara() # Output: Kucing Kiki sedang makan: tulang
hewan2.bersuara() # Output: Anjing Ichi bersuara: Guk Guk!
hewan2.bersuara() # Output: Anjing Ichi sedang makan: tulang
'''

class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        pass

    def makan(self):
        print(f"{self.__class__.__name__} {self.nama} sedang makan: tulang")

    def minum(self):
        print(f"{self.__class__.__name__} {self.nama} sedang minum")

class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.__class__.__name__} {self.nama} bersuara: Meong!")

class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.__class__.__name__} {self.nama} bersuara: Guk Guk!")

#Input dan Output yang muncul
hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama)  # Output: Kiki
print(hewan2.nama)  # Output: Ichi

hewan1.bersuara()   # Output: Kucing Kiki bersuara: Meong!
hewan1.makan()      # Output: Kucing Kiki sedang makan: tulang
hewan2.bersuara()   # Output: Anjing Ichi bersuara: Guk Guk!
hewan2.makan()      # Output: Anjing Ichi sedang makan: tulang
