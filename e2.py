import productos
def seleccionar_productos():
    products = []
    disponibles =productos.get_products() 
    print(disponibles)
    while True:
        try:
            id = input("ingrese el Id del producto que desea seleccionar")
            producto = disponibles[id]
            cantidad = int(input("ingrese el Id del producto que desea seleccionar"))
            producto["cantidad"] = cantidad
            products.append(producto)
        except:
            print ("Id inválido")
        continuar = input("Desea agregar otro producto (y/n)").lower()
        while continuar != 'y' and continuar != 'n':
            print ("opcion invalida")
            continuar = input("Desea agregar otro producto (y/n)").lower()
        if continuar == 'n':
            break
    return productos

def menu_usuario(usuarios):
    while True:
        try:
            cedula = int(input("Ingrese su cedula: "))

            nombre = input("Ingrese su nombre: ")

            tipo_envio = input("Ingrese su tipo de envío:\nAereo (a)\nMaritimo (m)").lower()                        
            if tipo_envio != 'a' and tipo_envio != 'm':
                print('Ingresa una opcion valida')
                raise Exception

            metodo_pago = input("Ingrese el metodo de pago").lower()
            if tipo_envio != 'h' and tipo_envio != 'j':
                print('Ingresa una opcion valida')
                raise Exception        

            productos = seleccionar_productos()

            reembalar = input("Desea reembalaje (y/n").lower()
            if reembalar != 'y' and reembalar != 'n':
                print('Ingresa una opcion valida')
                raise Exception
        
            seguro = input("Desea seguro (y/n").lower()
            if seguro != 'y' and seguro != 'n':
                print('Ingresa una opcion valida')
                raise Exception
            
            usuario = {}
            usuario['cedula'] = cedula
            usuario['nombre'] = nombre
            usuario['tipo_envio'] = tipo_envio
            usuario['metodo_pago'] = metodo_pago
            usuario['reembalar'] = reembalar
            usuario['seguro'] = seguro
            usuario['productos'] = productos
            usuario['costo'] = calcular_costo(usuario)

            continuar = input('Desea añadir otro usuario? (y/n)').lower()
            while continuar != 'y' and continuar != 'n':
                print("opcion invalida")
                continuar = input('Desea añadir otro usuario? (y/n)').lower()            
            if continuar == 'n':
                break            
        except:
            print('Error')
    def calcular_costo(usuario):
        cobro = 0
        if usuario['tipo_envio'] == 'a':
            cobro = calcular_envio(productos, 4)
        else:
            cobro = calcular_envio(productos,2)

        precio = calcular_precio(productos)
        if usuario ['reembalar'] == 'y':
            cobro += precio *0.03

        if usuario ['seguro'] == 'y':
            cobro += precio *0.01 
        return cobro

def calcular_envio(productos,tasa):
    envio = 0
    

def calcular_precio(productos):
    break

def menu_admin(usuarios):
    envio_maritimo = list(filter(lambda p: p['tipo_envio'] == 'm', usuarios))
    envio_aereo = list(filter(lambda p: p['tipo_envio'] == 'a', usuarios))
    cantidad_maritimo = len(envio_maritimo)
    cantidad_aereo = len(envio_aereo)
    ganancia_maritimo=0
    ganancia_aereo=0
    for(i in envio_maritimo):
        ganancia_maritimo += i['costo']

     for(i in envio_aereo):
        ganancia_aereo += i['costo']
       
    print("encomiendas totales de envio maritimo {cantidad_maritimo}")
    print("encomiendas totales de envio aereo {cantidad_aereo}")
    print("ganancias por envio maritimo {ganancia_maritimo}")
    print("ganancias por envio aereo {ganancia_aereo}")
    
    filtar = input("desea filtrar por cédula (y/n)")
    while filtar != 'y' and filtar != 'n':
        print("opcion invalida")
        filtar = input("desea filtrar por cédula (y/n)")
        if(filtrar == 'n')
            return
        while True:
            ci = int (input("Ingrese la cedula"))
            usuarios_filrado = list(filter(lambda p: p['cedula'] == ci, usuarios))
            print(usuarios_filrado)
            continuar = input("desea filtrar por cédula (y/n)")
            while continuar != 'y' and continuar != 'n':
                print("opcion invalida")
                filtar = input("desea filtrar por cédula (y/n)")
            if(continuar == 'n')
                return


            
def main():
    usuarios= []
    while True:
        opcion = input('''
            Bienvenido a UNimet Express
            1. Ingresar como usuario
            2. Ingresar como administrador
            3. Salir
            > ''')
        if opcion == '1':
            menu_usuario(usuarios)          
        elif opcion == '2':
            menu_admin(usuarios)      
        elif opcion == '3':
            print("Adios!")
            break
        else:
            print ("Opción inválida")
            

main()