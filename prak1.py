# Inisiasi
a = int(input("masukkan detik: "))

# Proses
hasil = int(a/3600)
print(hasil, "jam")
a = a - hasil * 3600
hasil = int(a/60)
print(hasil, "menit")
a = a - hasil * 60
hasil = a

# Output
print(hasil, "detik")
