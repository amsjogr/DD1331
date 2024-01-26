#Amanda Sjogren, 971029, CFATE
#L1
a = float(input('Ange belopp: '))
b = float(input('Ange tid (i ar): '))
c = float(input('Ange sparranta (i procent): '))


def slutvarde(a,b,c):
 return a * (1+(c/100))**b

varde =str(slutvarde(a,b,c))
print('Slutvardet blir ' + varde)




r = float(input('Ange avstand i miljoner meter: '))
t = float(input('Omloppstid i dagar:  '))
pi=(3.141592653589793)
G= float(6.67*(10**-11))


def massa(r, t):
  R = (r * (10**6))
  T = (t * 24 * 60 * 60)
  m= float((4*pi*pi*R*R*R) / (G*T*T))
  return m

M=str(massa(r,t))
print('Massan blir ' + M + 'kg')
