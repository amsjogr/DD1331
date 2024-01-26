#L2
#Amanda Sjogren 971029. CFATE

import statistics

def inmatning(b):

      res = ([])

      for x in range(b):
         q = str(x + 1)
         p = float(input('Ange for deltagare ' + q))
         res.append(p)

      return res

def statistik(c):
       sa=str(statistics.stdev(c))
       medel= str(statistics.mean(c))
       topp= str(max(c))
       minu= str(min(c))
       print('Medelvardet ar '+ medel+'m med standardavvikelse ' +sa+'m. Hogsta varde var '+ topp+'m och det lagsta ' +minu+'m')
       return 
T = 1
while T == 1:

     print('Meny')
     print('1 - Mata in de tavlandes resultat.')
     print('2 - Se statistik for tidigare inmatade.')
     print('3 - Avsluta.')
     a = int(input('Ange val: '))

     if a == 1:
       b = int(input('Ange hur manga tavlande: '))
       lista = inmatning(b)
     if a == 2:
       statistik(lista)
     if a == 3:
        T = 2
     else:
         print('Valj 1, 2 eller 3')
