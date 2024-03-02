batas_Bawah = int(input("Batas bawah : "))
batas_Atas = int(input("Batas atasa : "))
sum = 0
if batas_Bawah >= 0 and batas_Atas >= 0 : 
    for i in range(1, batas_Atas):
        if i % 2 != 0:
            print(i)
        sum += 1
    print("Total :", sum)
else:
    print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah NOL")