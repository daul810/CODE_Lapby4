nama = input("Masukan Nama:")
nim = input("Masukan NIM:")
uts = input("Masukan Nilai UTS:")
uas = input("Masukan Nilai UAS:")
tugas = input("Masukan Nilai Tugas:")

akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)

print("\nNama               :",nama)
print("\nNIM                :",nim)
print("Nilai UTS            :",uts)
print("Nilai UAS            :",uas)
print("Nilai Tugas          :",tugas)
print("Nilai Akhir          :",akhir)

print ('')
print ('Tambah Data? (ya/tidak)')
x=input()