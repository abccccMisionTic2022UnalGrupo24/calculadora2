sencilla = 20000
doble = 25000
triple = 28000
total = 0
l_prod = []
l_total = []
l_cantidad = []
contar=[]
caso=False
cont=0
bebidadulce = (3000 * 1.19)
cerveza = (4000*1.19)
cantidad=0
agua= 4000
c=0
r=0
d=0
e=True
beb=[]
canbeb=[]


def ivad(bebidadulce,cantidad):
    text="Gaseosas o Jugos "
    beb.append(text)
    canbeb.append(cantidad)
    gascan = bebidadulce * cantidad
    totalconiva= (gascan*1.19)
    return totalconiva

def ivac(cerveza,cantidad):
    text="Cervezas"
    beb.append(text)
    canbeb.append(cantidad)
    cercan = cerveza * cantidad
    totalconivac= (cercan*1.19)
    return totalconivac

def siniva(agua,cantidad):
    text="Agua"
    beb.append(text)
    canbeb.append(cantidad)
    agu = agua * cantidad
    totalsinivac= (agu*1.19)
    return totalsinivac

"""while e==True:
    Entradadetexto=input("Ingrese el tipo de bebidas que desea: \n 1 Gaseosa o Jugo \n 2. Agua  \n 3. Cerveza \n C. Continuar \n Ingrese el tipo segun se espeficica y la cantidad: ")
    Entradadetexto=Entradadetexto.lower()



    if (Entradadetexto == "1" or Entradadetexto=="gaseosa"):
        cantidad=int(input("Ingrese la contidad de bebidas que desea: "))
        r= ivad(bebidadulce,cantidad)
    elif (Entradadetexto == "3" or Entradadetexto=="cerveza"):
        cantidad=int(input("Ingrese la contidad de bebidas que desea: "))
        c= ivac(cerveza,cantidad)
    elif (Entradadetexto == "2" or Entradadetexto=="agua"):
        cantidad=int(input("Ingrese la contidad de bebidas que desea: "))
        f=siniva(agua,cantidad)
    else:
        print(" Bebidas confirmadas!!!!")      
        e=False
"""
def Eliminar():
    for i in range(len(l_prod)):
        print(i+1,l_cantidad[i], l_prod[i], l_total[i])
    l=int(input("Indique el producto que desea eliminar:"))
    l=l-1
    #if (delete == "hamburguesa sensilla" or delete == "sensilla" or delete == "1"):
     #   remo="Hamburguesa Sencilla"
      #  for i in range((len(l_prod))):
       #     remo2=l_prod[(i-1)]
         #   print(remo)
          #  if (remo == remo2):

    del l_prod[l]
    del l_cantidad[l]
    del l_total[l]
    for i in range(len(l_prod)):
        print(i+1,l_cantidad[i], l_prod[i], l_total[i])
    #    caso = True        
        
    
def add(texto,c):
    cantidad = int (input("Cantidad de Hamburguesas: "))
    tot = c * cantidad  
    cont=+1
    l_prod.append(texto)
    l_total.append(tot)
    l_cantidad.append(cantidad)
    contar.append(cont)
    op = input("Desea ordenar algo mas? oprima S o N: ").upper()
    if (op == "S"):
        caso = False
        Menu(caso)
    else:
        caso = True
        print("Lo que usd ordeno fue:\n ------------------------------")
        for i in range(len(l_prod)):
            print(i+1,l_cantidad[i], l_prod[i], l_total[i])
        print("------------------------------ \n El valor total es: ", sum(l_total)) 
        check= (input(print(" ------------------------------ \n desea eliminar algun item S/N:  "))).upper()
        if (check == "S"):
            Eliminar()
            caso=True
          
                
def Menu(caso):
    print("1. Hamburguesa sencilla  ... $20.000 pesos")
    print("2. Hamburguesa doble     ... $25.000 pesos")
    print("3. Hamburguesa triple    ... $28.000 pesos" )
    print("4. Gaseosa o Jugo        ... $ 3.000 pesos")
    print("5. Cerveza               ... $ 4.000 pesos")
    print("6. Agua                  ... $ 4.000 pesos" )
    print("7. Eliminar Item de la orden")
    print("8. Salir para continuar con el medio de pago")
    opcion=caso
    while opcion==False:
        opcion_hamburguesa=input("CUAL DESEAS ORDENAR: ").upper()
        print("La opcion elegida fue: ", opcion_hamburguesa)

        if(opcion_hamburguesa == "1"):
            print("La hamburguesa que usted pidió fue: Hamburguesa sencilla, con un valor de $20.000 pesos")
            texto = "Hamburguesa Sencilla"
            c = sencilla
            add(texto,c)
        elif(opcion_hamburguesa == "2"):
            print("La hamburguesa que usted pidió fue: Hamburguesa doble, con un valor de $25.000 pesos")
            texto = "Hamburguesa_Doble"
            c = doble
            add(texto,c)
        elif(opcion_hamburguesa == "3"):
            print("La hamburguesa que usted pidió fue: Hamburguesa triple, con un valor de $28.000 pesos")
            texto = "Hamburguesa Triple"
            c = triple
            add(texto,c)
        elif(opcion_hamburguesa == "4"):
            print("Ha seleccionado Gaseosas o Jugos, con un valor de $3.000 pesos")
            texto = "Gaseosa o Jugo"
            c = bebidadulce
            add(texto,c)
        elif(opcion_hamburguesa == "5"):
            print("Ha seleccionado cerveza, con un valor de $4.000 pesos")
            texto = "Cerveza"
            c = cerveza
            add(texto,c)
        elif(opcion_hamburguesa == "6"):
            print("Ha seleccionado Agua, con un valor de $4.000 pesos")
            texto = "Agua"
            c = agua
            add(texto,c)
        elif(opcion_hamburguesa == "7"):
            Eliminar()
            caso-True
        elif(opcion_hamburguesa == "SALIR"):
            opcion = True
            for i in range(len(l_prod)):
                print(l_cantidad[i], l_prod[i], l_total[i])
            print("El valor total es: ", sum(l_total))    
        else:
            print("Por favor eligir una opción valida\n")

def mediopago():  
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
            print("por favor eligir una opción valida\n") 

print("Bienvenidos al restaurante hamburguers abcccc \nPor favor eliga una de las siguientes opciones para pedir una hamburguesa: ")
Menu(caso)
mediopago()