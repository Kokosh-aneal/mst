#! /usr/bin/python
import os
import subprocess

#kompilacja programu
#os.system("make clean")
#os.system("make")

mst = "./mst graf"

def wierzcholki(plik_tmp, k_tmp, w_tmp, krok, limit):
    plik_tmp.write("_| Stała ilość wierzchołków |_\n")
    plik_tmp.write("Krawędzie: {} ; Wierzchołki: {} ; Krok: {} ; Ilość: {}\n".format(k_tmp, w_tmp, krok, limit))
    for j in range(0,limit):
        graph = "./graphgen {} {} graf".format(w_tmp,k_tmp)
        os.system(graph)
        wynik = os.popen(mst).read()
        wynik_str = str(wynik)
        plik_tmp.write(wynik_str)
        k_tmp += krok

def krawedzie(plik_tmp, k_tmp, w_tmp, krok, limit):
    plik_tmp.write("_| Stała ilość krawędzi |_\n")
    plik_tmp.write("Krawędzie: {} ; Wierzchołki: {} ; Krok: {} ; Ilość: {}\n".format(k_tmp, w_tmp, krok, limit))
    for j in range (0,limit):
        graph = "./graphgen {} {} graf".format(w_tmp,k_tmp)
        os.system(graph)
        wynik = os.popen(mst).read()
        wynik_str = str(wynik)
        plik_tmp.write(wynik_str)
        w_tmp += 2000 

#plik = open("wynik_w.txt", "w")
#wierzcholki(plikk, 10000, 1000, 2000, 21000)
#plik.close()

#plik = open("wynik_k.txt", "w")
#krawedzie(plik, 10000, 1000, 2000, 10)
#plik.close()

for i in range(1,4):
    nazwa = "wynik_w{}.txt".format(i)
    plik = open(nazwa, "w")
    wierzcholki(plik, i*10000, i*1000, i*2000, 5)
    plik.close()

for i in range(1,4):
    nazwa = "wynik_k{}.txt".format(i)
    plik = open(nazwa, "w")
    krawedzie(plik, i*10000, i*1000, i*200, 5)
    plik.close()