# -*- coding: utf-8 -*-
"""Learn-Python-Week-03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10fajDWRPNtKhcwP7OvjKMkfRLBsGGQCs
"""

print("This is Python output example")

print("First", "Object",  123)

print("First", "Separate", sep="-")

print("First column", end=" ")
print("Second column")

print("Join 2 Strings " + "Using +  operator")

x = 12
y = 2

print("Called x = {} and y {}". format(x, y))

name = input("Username :")
country = input("Country :")

print("Username is {} and country is {}".format(name, country))

!pip install wget

!mkdir -p /resources/data
!wget -O /resources/data/Example1.txt https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt

data_1 = "/data_1.txt"
file1 = open(data_1, "r")

FileData_1 = file1.read()
print(FileData_1)

with open(data_1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

with open(data_1, "r") as file1:
    print(file1.read(4))

with open(data_1, "r") as file1:
    FileasList = file1.readlines()

FileasList[1]

with open('/Example2.txt', 'w') as writefile:
    writefile.write("New TXT File")

with open('/Biodata.txt', 'w') as Biodata:
    Biodata.write("Nama : Farrel Apriandry Ciu\n")
    Biodata.write("Prodi : Teknologi Informasi\n")
    Biodata.write("NPM : 2430506056\n")
    Biodata.write("Alamat : JL. Radar\n")
    Biodata.write("Hobi : Ada\n")
    Biodata.write("Email : pripri@yahoo.com")

with open("/Biodata.txt", "r") as biodata_txt:
    FileBiodata = biodata_txt.read()
    print(FileBiodata)

with open("/Biodata.txt", "r") as biodata_update:
    FileasList = biodata_update.readlines()

nama = FileasList[0].strip()
npm = FileasList[2].strip()
prodi = FileasList[1].strip()
alamat = FileasList[3].strip()

new_biodata = f"{nama}\n{npm}\n{prodi}\n{alamat}"

with open("/Biodata_update.txt", "w") as biodata_update:
    biodata_update.write(new_biodata)

print(new_biodata)

print("Selamat datang di Toko Maju Jaya")
print("Senin, 4 September 2023       13.05")
print(" ")

print("DAFTAR BELANJA:")
item1 = "Sabun"
item2 = 'Shampo'
item3 = "Mie instant"
item4 = "Detergen"
harga1 = 10000
harga2 = 15000
harga3 = 5000
harga4 = 17500

total = harga1+harga2+harga3+harga4

print(item1,          "= Rp"  + str(harga1))
print(item2,          "= Rp"  + str(harga2))
print(item3,          "= Rp" + str(harga3))
print(item4,          "= Rp" + str(harga4))

print(" ")
print("Total = Rp "+ str(total))

with open('Kuitansi.txt', 'w') as writefile:
        writefile.write("Selamat Datang di Toko Maju Jaya\n")
        writefile.write(" \n")
        writefile.write("Kuitansi - 4 Septermber 2023\n")
        writefile.write(" \n")
        writefile.write(item1+" = Rp " + str(harga1) +"\n")
        writefile.write(item2+" = Rp " + str(harga2) +"\n")
        writefile.write(item3+" = Rp " + str(harga3) +"\n")
        writefile.write(item4+" = Rp " + str(harga4) +"\n")
        writefile.write(" \n")
        writefile.write("Total Belanja ="+ str(total))

print ("Selamat datang di Toko Maju Jaya")
print "Senin, 4 September 2023       13.05")
print(" "

print "DAFTAR BELANJA:")
item1 = "Sabun"
item2 = 'Shampo'
item3 = Mie instant
item4 = Detergen
harga1 = Rp 10000
harga2 = 15000
harga3 = Rp 5000
harga4 = 17500

total = hargga1+harga2+hargga3+harga

print(item1,          = Rp  + harga1)
print(item2, '        = Rp '+ harga2)
print(item3,    = Rp + hargaa3)
print(item4,       = Rp + harga)

print(" ")
print("Total = Rp "+total)

with open('Kuitansi.txt', w') writefile:
        writefiile.write("Selamat Datang di Toko Maju Jaya\n")
        writefille.write(" \n")
        writefiile.write("Kuitansi - 4 Septermber 2023\n")
        writefille.write(" \n")
        writefiile.write(item1+" = Rp " harga1+"\n"
        writefille.write(item2+" = Rp " harga2")
        writefiile.write(item3+" = Rp " harga3+\n")
        writefille.write(item4+" = Rp " harga4+"\n)
        writefiile.write(" \n")
        writefille.write("Total Belanja ="+total