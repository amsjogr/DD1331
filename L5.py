#L5 Amanda Sjogren 971029, CFATE
# -*- coding: utf-8 -*-

class aminosyror:  #Skapar alla egenskaper hos aminosyran
    def __init__(self, fil):
     nm = fil.readline().rstrip('\n') #En aminosyra i taget i textfilen
     nmr = nm.split( )
     self.code = nmr[0]
     self.name = nmr[1]
     self.group = nmr[2]
     self.mm = float(nmr[3])

    def __repr__(self):
     return repr((self.code, self.name, self.group, self.mm)) #Så en aminosyra är ett element

def list(path): #Skapar listan med aminosyror
    fil = open(path, 'r')
    lis = []

    for i in range(20):
        k = aminosyror(fil)
        lis.append(k)

    return lis

def sortering(a,lista): #Sorterar listan beroende på val
    if a == 1:
      pp = sorted(lista, key=lambda aminosyror: aminosyror.code)
    if a == 2:
      pp = sorted(lista, key=lambda aminosyror: aminosyror.name)
    if a == 3:
      pp = sorted(lista, key=lambda aminosyror: aminosyror.group)
    if a == 4:
      pp = sorted(lista, key=lambda aminosyror: aminosyror.mm)
    return pp



def main():

 T = 0
 path = 'aminosyror.txt' #path till filen
 lista = list(path)
 while T < 1: #Infinite loop

   print('1 - print table of aminoacids sorted by code')
   print('2 - print table of aminoacids sorted by name')
   print('3 - print table of aminoacids sorted by group')
   print('4 - print table of aminoacids sorted by mm')
   print('5 - quit')

   u = input('Choose number: ')

   if u == 1 or u == 2 or u == 3 or u == 4:
    ppp = sortering(u,lista)
    for i in range (20):
      o = str(ppp[i])
      print o.strip('()')

    T = 2

   if u == 5: #Valet att avsluta

    T = 2

   else: # Om man skriver in en siffra som inte är i menyn börjar den om
    pass
main()