nama = "Ramdani"
umur = 20

pesan = "Halo nama saya " + nama + ", umur saya " + str(umur) + " tahun."
print(pesan)
length = len(pesan)
print("Panjang string pesan adalah:", length)
print(len(nama))

kalimat = "Baris Pertama\nBaris Kedua\nBaris Ketiga"
print(kalimat)

data = "Nama saya adalah Ramdani\tSaya berumur 20 tahun."
print(data)

#string interpolation
nama = "Ramdani"
umur = 20
asal = "Indonesia"
pesan = f"Halo nama saya {nama}, umur saya {umur} tahun, saya berasal dari {asal}."
print(pesan)
pesan = f"Halo nama saya {nama}, umur saya {umur} tahun."
print(pesan)


harga = 10000
jumlah = 5
total= f"Harga total adalah Rp {harga * jumlah}"
print(total)