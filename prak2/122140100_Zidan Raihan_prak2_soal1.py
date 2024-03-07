'''
Buatlah program python yang memiliki class Mahasiswa
dengan properties nim, nama, angkatan, isMahasiswa. Buatkan minimal 3 method
yang melakukan suatu operasi dan mengembalikkan suatu nilai (return). Object
yang diinisiasikan minimal 2 dengan value properties yang berbeda. Gunakan default
value parameter pada class untuk properties isMahasiswa kemudian coba hilangkan
parameter untuk isMahasiswa saat ingin menginisiasi object kedua. Diwajibkan menggunakan setter getter 
(fungsi ini tidak termasuk kedalam 3 method yang diminta) untuk mengambil dan mengganti 
nilai properties private yaitu nama dan nim.
'''


class Mahasiswa:
    
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def jumlahSemester(self):
        semester = 0
        tahunSekarang = 2024
        if(self.isMahasiswa == True):
            if tahunSekarang - self.angkatan == 0:
                semester += 1
                return f"Jumlah semester adalah {semester} semester"
            else:
                semester = 2 * (tahunSekarang - self.angkatan)
                return f"Jumlah semester adalah {semester} semester"

    def showData(self):
        return f"Nama\t : {self.__nama}\nNIM\t : {self.__nim}\nAngkatan : {self.angkatan}"

    def cekMahasiswa(self, isMahasiswa):
        if self.isMahasiswa == False:
            return f"{self.__nama} Bukan mahasiswa asli"
        else:
            return f"{self.__nama} Mahasiswa asli"

    def ubahNIM(self, nim_baru):
        self.__nim = nim_baru
        return f"NIM diubah menjadi {self.__nim}"

    def get_cekNim(self):
        if self.__nim % 2 == 0:
            return f"Mahasiswa dengan nama ({self.__nama}) NIM ({self.__nim}) memiliki nilai NIM Genap"
        else:
            return f"Mahasiswa dengan nama ({self.__nama}) NIM ({self.__nim}) memiliki nilai NIM Ganjil"


mahasiswa1 = Mahasiswa(123456789, "Budi", 2023)
mahasiswa2 = Mahasiswa(123456796, "Zidan", 2023, False)
mahasiswa3 = Mahasiswa(123457683, "Tiara", 2022)
print("============================")
print(mahasiswa1.showData())
print(mahasiswa1.get_cekNim())
print(mahasiswa1.cekMahasiswa(mahasiswa1.isMahasiswa))
print(mahasiswa1.jumlahSemester())
print("============================")

print(mahasiswa2.showData())
print(mahasiswa2.get_cekNim())
print(mahasiswa2.cekMahasiswa(mahasiswa2.isMahasiswa))
print(mahasiswa2.jumlahSemester())
print("============================")

print(mahasiswa3.showData())
print(mahasiswa3.get_cekNim())
print(mahasiswa3.cekMahasiswa(mahasiswa3.isMahasiswa))
print(mahasiswa3.jumlahSemester())
