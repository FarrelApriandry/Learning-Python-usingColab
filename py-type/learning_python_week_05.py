# -*- coding: utf-8 -*-
"""Learning-Python-Week05.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AZX2jk5SmGg_wUmRDeqh8hFS8fuWyeDg
"""

#Age Checker

age = 16

if num > 21:
    print("All item is legal.")
else:
    if num > 17:
        print("Not all item is legal.")
    else:
        print("Not met the requirement.")

username = str(input("Enter Username: "))
password = str(input("Enter Password: "))

if username and password == "admin":
    print("Berhasil login sebagai admin")
elif username == "admin" and password == "12345":
    print("Kata sandi lemah, ata sandi perlu dirubah")
elif username == "guest" and password == "guest":
    print("Berhasil login sebagai guest")
elif username == "guest" and password != "guest":
    print("Password salah!")
else:
    print("Anda belum paham cara mainnya!")

num = int(input("Masukkan angka: "))

if type(num) == int :
  if num > 0:
    if num % 2 == 0:
      print("angka merupakan bilangan genap")
    else:
      print("ankga merupakan bilangan ganjil")
  elif num < 0:
    print("angka merupakan bilangan bulat negatif")
  else:
    print("angka merupakan nol")
else:
  print("angka bukan bilangan bulat")

try:
    num = int(input("Masukkan angka: "))

    if num > 0:
        if num % 2 == 0:
            print("Angka merupakan bilangan genap")
        else:
            print("Angka merupakan bilangan ganjil")
    elif num < 0:
        print("Angka merupakan bilangan bulat negatif")
    else:
        print("Angka merupakan nol")

except ValueError:
    print("Angka bukan bilangan bulat")