print("hola")
print("ara dues linies\nAra la segona")
numero=10
print(numero)
print(type(numero))
numero2=10.2
print(numero2)
print(type(numero2))

cadena1='a'
print(cadena1)
print(type(cadena1))
cadena2="ppa"
print(cadena2)
print(type(cadena2))
cadena3="yo estoy 'estudiando'"
print(cadena3)

valor= True
print (valor)
print (type(valor))

a=16
b=14.5
suma=a+b
print (suma)
resultat= (a+b)/10*3
print ("el resultat es ",resultat)
# comentari d'una línia
'''ara
podem
fer un comentari simple nomes al principi
possant 3 comentes sencilles'''
#operadors aritmètics
a=5
b=2
suma=a+b
print (suma)
divisio = a/b
divisiosencera= a//b
rmodul=a%b
exponencia=a**b
print ("divisio",divisio)
print ("sencera",divisiosencera)
print ("modul",rmodul)
print ("potencia",exponencia)

#operadors aritmetics s'executen ABANS que els relacionals
#operadors: > >= < <= == !=

resultat= 10 < 20
print (resultat)
resultat = 10 !=10
print (resultat)
a=20
b=22
c=32
resultat = a+b ==c
print (resultat)
#operador logics  and  or not
#ordre  1er evaluar Not, and or

#prioritat de tots els operadors
'''
1)  ()
2)  **
3) *  /  mod  not
4) +  -  and
5) > < == >= <= != or
'''
a=10
b=15
c=20
resultat=(a<b) and (b<c)
print (resultat)

#operadors d'assignacio
a=a+5
print (a)
a +=5
print (a)
a -=3
print (a)
a *=4
print (a)
a /=3
print (a)
a**=2
print (a)
a%=2
print(a)

#format
nombre ="pepe"
edad =22
print ("Hola {}  com estas tens {} anys".format(nombre, edad))

print (f"hola {nombre} tens {edad} anys")
#alerta la f després del print (

#entrada de datos de tipus cadena
nombre =input("escriu el teu nom: ")
print (f"hola {nombre}")

#entrada de datos de tipus numero
numero = int(input("quin numero es: "))
print (numero)

#entrada float
numero = float ( input ("numero float"))
print (numero)
