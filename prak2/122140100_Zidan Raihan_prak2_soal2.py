'''
Buatlah program python yang memiliki class (bebas). 
Program harus menerapkan decorator, constructor, dan destructor. 
Masing-masing praktikan tidak boleh memiliki konsep yang sama!.
'''
# INDEX MASSA TUBUH(IMT)


class IMT:
    def __init__(self, function):
        self.function = function

    def __call__(self, nama, berat, tinggi):
        index = self.function(nama, berat, tinggi)
        if index > 40:
            return f"Nama\t\t : {nama}\nBerat Badan\t : {berat} kg\nTinggi Badan\t : {tinggi} cm\nIMT\t\t : {index}\nKategori\t : Dengan IMT {index} anda masuk\n\t\t   ke dalam kategori Obesitas Kelas 3"
        elif index > 35 and index < 39.9:
            return f"Nama\t\t : {nama}\nBerat Badan\t : {berat} kg\nTinggi Badan\t : {tinggi} cm\nIMT\t\t : {index}\nKategori\t : Dengan IMT {index} anda masuk\n\t\t   ke dalam kategori Obesitas Kelas 2"
        elif index > 30 and index < 34.9:
            return f"Nama\t\t : {nama}\nBerat Badan\t : {berat} kg\nTinggi Badan\t : {tinggi} cm\nIMT\t\t : {index}\nKategori\t : Dengan IMT {index} anda masuk\n\t\t   ke dalam kategori Obesitas Kelas 1"
        elif index > 25 and index < 29.9:
            return f"Nama\t\t : {nama}\nBerat Badan\t : {berat} kg\nTinggi Badan\t : {tinggi} cm\nIMT\t\t : {index}\nKategori\t : Dengan IMT {index} anda masuk\n\t\t   ke dalam kategori Overweight"
        elif index > 18.5 and index < 24.9:
            return f"Nama\t\t : {nama}\nBerat Badan\t : {berat} kg\nTinggi Badan\t : {tinggi} cm\nIMT\t\t : {index}\nKategori\t : Dengan IMT {index} anda masuk\n\t\t   ke dalam kategori Normal"
        elif index < 18.5:
            return f"Nama\t\t : {nama}\nBerat Badan\t : {berat} kg\nTinggi Badan\t : {tinggi} cm\nIMT\t\t : {index}\nKategori\t : Dengan IMT {index} anda masuk\n\t\t   ke dalam kategori Kurus"

@IMT
def inputData(nama, berat, tinggi):
    index = berat/(tinggi/100)**2
    return index

print("===============================")
print(inputData("Zidan", 65, 172))
print("===============================")
print(inputData("Fitri", 78, 160))
print("===============================")
print(inputData("Ahmad", 90, 180))
print("===============================")