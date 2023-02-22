pkajsf = (input("Masukkan Plat Nomor : ")).split(" ")
try :
    akajuf = int(pkajsf[1])
    if akajuf <= 3000:
        print ("Plat nomor tersebut diperuntukan untuk mobil")
    elif akajuf <= 4000:
        print ("Plat nomor tersebut diperuntukan motor")
    elif akajuf <= 5000:
        print ("Plat nomor tersebut diperuntukan untuk angkutan umum")
    else:
        print ("Plat nomor tidak terindikasi ketiga angkutan tersebut")
except:
    print ("Plat Nomor Tidak Teridentifikasi, setelah kode daerah harus berupa nomor kendaraan")