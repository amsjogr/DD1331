#L4 Amanda Sjogren 971029, CFATE
# -*- coding: utf-8 -*-

class lander:
    def __init__(self, fil):
     nmr = fil.readline().rstrip('\n') #Ett land i taget, radvis
     data = nmr.split(',') #Separerar datan för landet
     self.land = data[0] #Landets namn
     self.ytan = float(data[1]) #Landets yta
     self.folkmangd = float(data[2]) #Landets folkmängd
     self.befoltat()

    def __str__(self):
     return( str(self.land) + ' ' + str(self.folkmangd) + ' ' + str(self.ytan) + ' ' + str(self.bef))

    def befoltat(self):
     self.bef = self.folkmangd / self.ytan


def main():

 path='europa.txt'
 fil = open(path, 'r')
 for i in range(50):
     pp = []
     pp.append(str(lander(fil)))
     print pp

main()


