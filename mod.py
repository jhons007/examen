import sys,os,time
def verificar(x):
    for c in x:
        if(ord(c)<65 or ord(c)>90)and (ord(c)<97 or ord(c)>122) and(ord(c)!=32):
            return False
    return True
def nnmobre():
    global nombre
    print("ingrese su nombre")
    nombre=input()
    while(not verificar(nombre)):
        print("ingrese correctamente su nombre")
        nombre=input()

def nedad():
    global edad
    while(1):
        try:
            print("ingrese su edad ")
            edad=input()
            edad=int(edad)
            while(edad<0 or edad>150):
                print("ingrese su edad correctamente")
                edad=input()
                edad=int(edad)
            break
        except ValueError:
            print("ingrese correctamente su edad")
def nreporte():
    os.system("clear")
    print("********reporte******")
    print("NOMBRE     :",nombre)
    print("DNI     :",dni)
    print("EDAD     :",edad)
    print("TIPO      :",cambio,"%",)
    print("MONTO DE FONDO",fondo,"S/")
    time.sleep(4)


def ndni():
    global dni
    global cambio
    dat_dni=""
    while(1):
        try:
            print("ingrese su dni")
            dni=input()
            dni=int(dni)
            while(len(str(dni))!=8):
                print("ingrese de un tamaño de  8 digitos")
                dni=input()
                dni=int(dni)
            data_dni=str(dni)
            break
        except ValueError:
            print("ingrese correctamente su dni")
    if(data_dni[0:2]=="01"):
        cambio=4
    elif(data_dni[0:2]=="29"):
        cambio=4
    else:
        cambio=2
        
def nfondo():
    global fondo
    while(1):
        try:
            print("ingrese su fondo")
            fondo=input()
            fondo=int(fondo)
            while(fondo<0):
                print("ingrese correctamente")
                fondo=input()
                fondo=int(fondo)
            break
        except ValueError:
            print("ingrese correctamente")


def nretiro():
    os.system("clear")
    global fondo
    print("CUENTA CON UN SALDO DE",fondo,)
    global retiro
    while(1):
        try:
            print("ingrese su monto de retiro")
            retiro=input()
            retiro=int(retiro)
            while(retiro<0 or retiro>fondo):
                print("ingrese correctamente no tiene saldo")
                retiro=input()
                retiro=int(retiro)
            break
        except ValueError:
            print("ingrese correctamente")
    fondo=fondo-retiro

    print("******banco SARITA****")
    print("NOMBRE            :",nombre)
    print("DNI               :",dni)
    print("SALDO TOTAL       :",fondo)
    print("RETIRO            :",retiro)
    time.sleep(4)
def ndeposito():
    os.system("clear")
    global deposito
    global fondo
    print("CUENTA CON UN SALDO DE",fondo,)
    while(1):
        try:
            print("ingrese su monto de deposito")
            deposito=input()
            deposito=int(deposito)
            while(deposito<0 ):
                deposito=input()
                deposito=int(deposito)
            break
        except ValueError:
            print("ingrese correctamente")
    fondo=fondo+deposito

    print("******BANCO SARITA****")
    print("NOMBRE            :",nombre)
    print("DNI               :",dni)
    print("SALDO TOTAL       :",fondo)
    print("DEPOSITO          :",deposito)
    time.sleep(4)

def nprestamo():
    os.system("clear")
    global prestamo
    while(1):
        try:
            print("ingrese su prestamo")
            prestamo=input()
            prestamo=int(prestamo)
            while(prestamo<0):
                print("ingrese correctamente su prestamo")
                prestamo=input()
                prestamo=int(prestamo)
            break
        except ValueError:
            print("ingrese correctamente")
    nmeses()

def nmeses():
    global meses
    while(1):
        try:
            print("ingrese su cantidad de meses")
            meses=input()
            meses=int(meses)
            while(prestamo<0):
                print("ingrese correctamente su cantidad de meses")
                meses=input()
                meses=int(meses)
            break
        except ValueError:
            print("ingrese correctamente")
    iprestamo()
def iprestamo():
    prestamot=prestamo+(prestamo*cambio/100*meses)
    mest=prestamot/meses
    print("prestamo total",prestamot,"S/")
    print("prestamo mensual",mest,"S/")
    time.sleep(4)
