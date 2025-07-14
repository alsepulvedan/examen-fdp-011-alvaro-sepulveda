from os import system

productos = {'8475HD':['HP',15.6,'8GB','DD','1T','Intel Core i5','Nvidia GTX1050'],
             '2175HD':['lenovo',14,'4GB','SSD','512GB','Intel Core i5','Nvidia GTX1050'],
             'JjfFHD':['Asus',14,'16GB','SSD','256GB','Intel Core i7','Nvidia RTX2080Ti'],
             'fgdxFHD':['HP',15.6,'8GB','DD','1T','Intel Core i3','integrada'],
             'GF75HD':['Asus',15.6,'8GB','DD','1T','Intel Core i7','Nvidia GTX1050'],
             '123FHD':['lenovo',14,'6GB','DD','1T','AMD Ryzen 5','integrada'],
             '342FHD':['lenovo',15.6,'8GB','DD','1T','AMD Ryzen 7','Nvidia GTX1050'],
             'UWU131HD':['Dell',15.6,'8GB','DD','1T','AMD Ryzen 3','Nvidia GTX1050']}

stock = {'8475HD':[387990,10],'2175HD':[327990,4],'JjfFHD':[424990,1],
        'fgdxFHD':[664990,21],'123FHD':[290890,32],'342FHD':[444990,7],
        'GF75HD':[749990,2],'UWU131HD':[349990,1],'FS1230HD':[249990,0]}

def limpiar_pantalla():
    try:
        system('cls')
        pass
    except:
        system('clear')

def menu():
    print("***MENU PRINCIPAL***")
    print("1. Stock marca.")
    print("2. Busqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    opcion()

def opcion():
    while True:
        try:
            opc = int(input("Ingrese opcion: "))
            if opc == 1:
                opc_1()
                break 
            elif opc == 2:
                opc_2()
                break
            elif opc == 3:
                opc_3()
                break
            elif opc == 4:
                print("Programa finalizado.")
                break
            else:
                print("El stock es 0 o el Modelo no ha sido encontrado.")
                break
        except ValueError:
            pass
def opc_1():
    while True:
        try:
            modelo = input("Ingrese modelo a consultar: ")
            if modelo == '8475HD':
                print(f"El precio/stock es: {stock['8475HD']}")
                break
            elif modelo == '2175HD':
                print(f"El precio/stock es: {stock['2175HD']}")
                break
            elif modelo == 'JjfFFHD':
                print(f"El precio/stock es: {stock['JjfFFHD']}")
                break
            elif modelo == 'fgdxFHD':
                print(f"El precio/stock es: {stock['fgdxFHD']}")
                break
            elif modelo == 'GF75HD':
                print(f"El precio/stock es: {stock['GF75HD']}")
                break
            elif modelo == '123FHD':
                print(f"El precio/stock es: {stock['123FHD']}")
                break
            elif modelo == '342FHD':
                print(f"El precio/stock es: {stock['342FHD']}")
                break
            elif modelo == 'UWU131HD':
                print(f"El precio/stock es: {stock['UWU131HD']}")
                break
        except ValueError:
            print("El Modelo no ha sido encontrado o el Stock es 0.")
            break
            


def opc_2():
    precio_minimo = input("Ingrese precio minimo: ")
    precio_maximo = input("Ingrese precio maximo: ")
    print("Los notebooks entre los precios consultas son: ")
    
def opc_3():
    modelo = input("Ingrese modelo a actualizar: ")
    precio_nuevo = input("Ingrese precio nuevo: ")

while True:
    try:
        menu()
    except:
        pass
    