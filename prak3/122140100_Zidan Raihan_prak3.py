'''
Buatlah sebuah kelas Dagangan yang memiliki atribut instance berupa nama,
stok, dan harga (bersifat private) yang nilainya tidak sama untuk tiap instansinya.
Selain itu, kelas Dagangan tersebut juga memiliki atribut kelas berupa
jumlah_barang dan list_barang (berisi data-data nama, stok, dan harga barang tiap
instansi) yang konsisten pada tiap instansi Dagangan yang telah dibuat. Gunakan
fungsi bantuan yaitu lihat_barang() untuk menampilkan output dari jumlah_barang
dan list_barang.
Contoh main program (kalian cukup buat kode untuk class Dagangan):
Dagangan1 = Dagangan(“Galon Aqua 19L”, 32, 17000)
Dagangan2 = Dagangan(“Gas LPG 5 kg”, 22, 88000)
Dagangan3 = Dagangan(“Beras Ramos 5 kg”, 13, 68000)
Dagangan.lihat_barang()
del Dagangan1
Dagangan.lihat_barang()
Output program tersebut (tiap instansi akan memberikan nilai konsisten satu sama
lain):
Jumlah barang dagangan pada toko: 3 buah
1. Galon Aqua 19L seharga Rp 17000 (stok: 32)
2. Gas LPG 5 kg seharga Rp 88000 (stok: 22)
3. Beras Ramos 5 kg seharga Rp 68000 (stok: 13)

Galon Aqua 19L dihapus dari toko!
Jumlah barang dagangan pada toko: 2 buah
1. Gas LPG 5 kg seharga Rp 88000 (stok: 22)
2. Beras Ramos 5 kg seharga Rp 68000 (stok: 13)
Gas LPG 5 kg dihapus dari toko!
Beras Ramos 5 kg dihapus dari toko!
'''


class Dagangan:
    jumlahBarang = 0
    listBarang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlahBarang += 1
        Dagangan.listBarang.append((nama, stok, harga))

    def __del__(self):
        Dagangan.jumlahBarang -= 1
        Dagangan.listBarang.remove((self.__nama, self.__stok, self.__harga))
        print(f"{self.__nama} dihapus dari toko!")

    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls.jumlahBarang} buah")
        for i, barang in enumerate(cls.listBarang, 1):
            nama, stok, harga = barang
            print(f"{i}. {nama} seharga Rp {harga} (stok: {stok})")

#MAIN
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()
del Dagangan1
Dagangan.lihat_barang()