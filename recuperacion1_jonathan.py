import sys,time,os
import mod
def menu():
    mod.nnmobre()
    mod.ndni()
    mod.nedad()
    mod.nfondo()
    opciones()

def opciones():
    os.system("clear")
    while(1):
        try:
            print("banco SARITA*****")
            print("1.-  reporte")
            print("2.-retiro/deposito")
            print("3.-prestamo")
            print("4.-salir")
            print("ingrese una opcion ")
            x=input()
            x=int(x)
            while(x<0 or x>4):
                print("ingrese correctamente la opcion de 1 a 4")
                x=input()
                x=int(x)
            break
        except ValueError:
            print("error opcion invalida vuelva intentar")
    if(x==1):
        mod.nreporte()
        opciones()
    elif(x==2):
        while(1):
            try:
                print("1.- deposito")
                print("2.- retiro")
                z=input()
                z=int(z)
                while(z<0 or z>2):
                    print("ingrese correctamente de 1 a 2")
                    z=input
                    z=int(z)
                break
            except ValueError:
                print("ingrese correctamente una opcion valida")
        if(z==1):
            mod.ndeposito()
            opciones()
        elif(z==2):
            mod.nretiro()
            opciones()
    elif(x==3):
        mod.nprestamo()
        opciones()
    elif(x==4):
        sys.exit()
            
                    
        
menu()
