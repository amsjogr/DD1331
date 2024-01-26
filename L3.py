#L3 Amanda Sjogren 971029, CFATE
# -*- coding: utf-8 -*-

def lista(P):

  fil = open(P,'r')
  data = file.read(fil)
  listan = data.split()
  return listan

def nylista(M,N):
    nylista = []
    for i in M:
        if i not in N:
            nylista.append(i)
    return nylista

def main():
 B = int(input('Vilken fil vill du lasa in?'))
 text = lista(B)
 antal = str(len(text))
 print ('Texten inehaller ' + antal + ' ord')
 vanliga = lista('vanligaord.txt')
 nylis = nylista(text,vanliga)
 antal2 = str(len(nylis))
 print ('Funnit ' + antal2 + ' ovanliga ord:')
 print nylis

main()

