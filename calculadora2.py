opcion=False

print("Bienvenidos al restaurante hamburguers abcccc \nPor favor eliga una de las siguientes opciones para pedir una hamburguesa: ")
print("1. Hamburguesa sencilla... $20.000 pesos")
print("2. Hamburguesa doble... $25.000 pesos")
print("3. Hamburguesa triple... $28.000 pesos" )

while opcion==False:
    opcion_hamburguesa=input("CUAL DESEAS ORDENAR: ")
    print("La opcion elegida fue: ", opcion_hamburguesa)

    if(opcion_hamburguesa == "1"):
        print("La hamburguesa que usted pidió fue: Hamburguesa sencilla, con un valor de $20.000 pesos")
    elif(opcion_hamburguesa == "2"):
        print("La hamburguesa que usted pidió fue: Hamburguesa doble, con un valor de $25.000 pesos")
    elif(opcion_hamburguesa == "3"):
        print("La hamburguesa que usted pidió fue: Hamburguesa triple, con un valor de $28.000 pesos")
    else:
        print("Por favor eligir una opción valida\n")

    
print("\nPor favor eliga el medio de pago con el cual usted va a cancelar su pedido por medio de las siguientes opciones: ")
print("1. Tarjeta de crédito (Se realiza un recargo del 7½)")
print("2. Otros medios de pago (no se realiza ningún tipo de recargo 0%)")
medio_de_pago=int(input())

while(medio_de_pago > 2):
    print("Por favor eligir una opción valida\n")
    print("\nPor favor eliga el medio de pago con el cual usted va a cancelar su pedido por medio de las siguientes opciones: ")
    print("1. Tarjeta de crédito (Se realiza un recargo del 7½)")
    print("2. Otros medios de pago (no se realiza ningún tipo de recargo 0%)")
    medio_de_pago=int(input())

if(medio_de_pago == 1):
    print("El medio de pago con el cual usted va a pagar es: Tarjeta de crédito, con un recargo del 7%")
elif(medio_de_pago == 2):
    print("El medio de pago con el cual usted va a pagar es: Otro medio de pago, con un recargo del 0%")
else:
    print("Por favor eligir una opción valida\n")
