A=int(20000)
B=int(25000)
C=int(28000)
Tipo= int()
N_Amburguesas= int() 

Tipo= int(input("Digite el valor de la amburguesa: "))
N_Amburguesas= int(input("Digite numero de amburguesas: "))
Valor_Recargo=Tipo*(N_Amburguesas*7)/100

print(f"El recargo de la tarjeta de credito es igual a: ${Valor_Recargo:.2f}")