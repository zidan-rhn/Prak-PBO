
class Pembayaran :
	def __init__(self, namaPelanggan, nomorPelanggan, jumlahTagihan) :
		self.namaPelanggan = namaPelanggan
		self.nomorPelanggan = nomorPelanggan
		self.jumlahTagihan = jumlahTagihan

		def hitung_biaya(self):
			 return self.jumlahtagihan
			
class Pembayaran_Internet(Pembayaran):
	def __init__(self, kecepatanInternet) :
		self.kecepatanInternet = kecepatanInternet

	def HitungBiaya(self) : 
		if self.kecepatanInternet <= 100 :
			return self.jumlahTagihan * 0.5
		elif self.kecepatanInternet <= 200 :
			return self.jumlahTagihan * 0.75
		else :
			return self.jumlahTagihan * 1.5
			
class Pembayaran_Listrik(Pembayaran) : 
	def __init__(self, penggunaanListrik) :
		self.penggunaanListrik = penggunaanListrik
		
	def HitungBiaya(self) :
		if self.penggunaanListrik <= 1000:
			return self.jumlahTagihan * 0.5
		elif self.penggunaanListrik <= 2000:
			return self.jumlahTagihan * 0.75
		else :
			return self.jumlahTagihan * 2

class Pembayaran_TVKabel(Pembayaran) :
	def __init__(self, paketTV) :
		self.paketTV = paketTV

	def HitungBiaya(self):
		if self.paketTV == "Biasa":
			return self.jumlahTagihan * 0.5
		elif self.paketTV == "Premium":
			return self.jumlahTagihan * 0.75
		
pembayaran1 = Pembayaran_Internet("Adi", "001", 500000, 200)
pembayaran2 = Pembayaran_Listrik("Adi", "002", 500000, 3000)
pembayaran3 = Pembayaran_TVKabel("Adi", "003", 500000, "Premium")

print("Nama Pelanggan : ", pembayaran1.namaPelanggan)
print("Nomor Pelanggan : ", pembayaran1.nomorPelanggan)
print("Jumlah Tagihan : ", pembayaran1.HitungBiaya())
print("Nama Pelanggan : ", pembayaran2.namaPelanggan)
print("Nomor Pelanggan : ", pembayaran2.nomorPelanggan)
print("Jumlah Tagihan : ", pembayaran2.HitungBiaya())
print("Nama Pelanggan : ", pembayaran3.namaPelanggan)
print("Nomor Pelanggan : ", pembayaran3.nomorPelanggan)
print("Jumlah Tagihan : ", pembayaran3.HitungBiaya())