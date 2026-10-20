import os
import time

conver = True

def menu():
    os.system('cls')
    print("""
    ====CONVERSOR DE MONEDAS====
----------------------------------
Escoja que moneda desea convertir:
----------------------------------
    1. Euro
    2. Dolar
    3. Yen
    4. Salir
==================================
    """)

def conversor(dinero="a",divisa=0):
    os.system('cls')
    print("    ===CANTIDAD A CONVERTIR===")
    print("-------------------------------------")
    print(f"Ingrese cuantos {dinero} desea convertir:")
    print("-------------------------------------")
    valor = float(input())  
    con = valor * divisa
    os.system('cls')
    print(f"""
        ===CONVERSION REALIZADA===
        
    {dinero}:""",f"{valor:,.2f}", "\n    Pesos Colombianos:", f"{con:,.2f}")

def men():
    print("""
        ====MENU====    
    1. Volver al menú
    2. Salir
""")
    
def marca():
    os.system('cls')
    print("\nGracias por usar nuestro conversor. Vuelva pronto!!\n")
    marca = [
    ("""     ==============
    |    Code by   |
    |    JORKENN   |
     ==============
    """,0.02)
    ]

    for letra, tiempo in marca:
        for let in letra:
            print(let, end="", flush=True)
            time.sleep(tiempo)
        
def divisa():
    moneda = int(input())
    while moneda > 4 or moneda <= 0:
        os.system('cls')
        menu()
        print("Ingrese una opcion valida\n")
        moneda = int(input())

    if moneda == 1:
        conversor(dinero="Euros",divisa=3670.30)
    elif moneda == 2:
        conversor(dinero="Dolares",divisa=3242.73)
    elif moneda ==3: 
        conversor(dinero="Yenes",divisa=20.52)
    else:
        return False

while conver:
    menu()
    salida = divisa()
    if salida == False:
        break
    else:
        men()
        opcion = int(input())
        while opcion > 2 or opcion <=0:
            os.system('cls')
            men()
            print("Ingrese una opcion valida")
            opcion = int(input())
        if opcion == 1:
            continue
        elif opcion ==2:
            break
 
marca()