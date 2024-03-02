def LuasLingkaran(phi, jarijari):
    return phi * jarijari**2


def KelilingLingkaran(phi, jarijari):
    return 2 * phi * jarijari


print("Menghitung Luas dan Keliling Lingkaran")
print("======================================")
phi = 3.14
jariJari = float(input("Masukan jari-jari : "))
if jariJari > 0:
    print(f"Luas : {LuasLingkaran(phi, jariJari)}")
    print(f"Keliling : {KelilingLingkaran(phi, jariJari)}")
else:
    print("Jari-jari lingkaran tidak boleh bernilai negatif(-)")
