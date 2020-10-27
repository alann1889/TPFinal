#! /usr/bin/env python3
import sys
from listaClientes import ListaClientes
from repositorioClientes import RepositorioClientes
from repositorio import Repositorio
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
class Menu:
    '''Mostrar un menú y responder a las opciones'''
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.recl = RepositorioClientes()
        self.repo = Repositorio()
        self.opciones= {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.actualizar_datos,
            "4": self.eliminar_cliente,
            "0": self.salir
        }

    def mostrar_menu(self):
        print("""
Menú del anotador:
1. Mostrar todos los clientes
2. Ingrese los datos del nuevo cliente
3. Actualizar datos de un cliente
4. Eliminar cliente
5. 
0. Salir
""")

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

    def mostrar_clientes(self, lista = None):
        if lista == None:
            lista = self.lista_clientes.lista
        for cliente in lista:
            print(cliente)

    def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo =  input("Ingrese el tipo de cliente: C: Corporativo / P: Particular: ")
        nombre = input("Ingrese el nombre del contacto: ")
        if tipo in ("C", "c"):
            contacto = input("Ingrese el nombre de la empresa: ")
            tc = int(input("Ingrese el telefono de la empresa: "))
        else:
            apellido = input("Ingrese el apellido: ")
        tel = int(input("Ingrese el telefono particular: "))
        mail = input("Ingrese el correo electronico: ")
        if tipo in ("C", "c"):
            c = self.lista_clientes.nuevo_cliente_corporativo(mail)
        else:
            c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido, tel, mail)
        if c is None:
            print("Error al cargar el cliente")
        else:
            print("Cliente cargado correctamente")



    def actualizar_datos(self):
        tipo = "A"
        id = int(input("Ingrese ID del cliente para actualizar sus datos: "))
        while tipo not in ("C", "c", "P", "p"):
            tipo =  input("Ingrese el tipo de cliente: C: Corporativo / P: Particular: ")
        nombre = input("Ingrese el nombre actualizado del contacto: ")
        if tipo in ("C", "c"):
            contacto = input("Ingrese el nombre actualizado  de la empresa: ")
            tc = int(input("Ingrese el telefono actualizado  de la empresa: "))
        else:
            apellido = input("Ingrese el apellido actualizado : ")
        tel = int(input("Ingrese el telefono particular actualizado : "))
        mail = input("Ingrese el correo electronico actualizado : ")
        if tipo in ("C", "c"):
            cliente = ClienteCorporativo(nombre, contacto,  tc, tel, mail, id)
            c = self.recl.update(cliente)            
        else:
            cliente = ClienteParticular(nombre, apellido, tel, mail, id)
            c = self.recl.update(cliente)  
        if c is None:
            print("Error al actualizar el cliente")
        else:
            print("Cliente actualizado correctamente")
        

    def  eliminar_cliente(self):
        id_cliente = int(input("Ingrese ID del cliente para eliminar sus datos: "))
        borrar = input("Para eliminar los datos del cliente ingrese E, de caso contrario se cancelará la eliminación: ")
        cliente = self.recl.get_one(id_cliente)
        if borrar == "E" or "e":
            c = self.recl.delete(cliente)
            print("El cliente se elimino correctamente! ")
        else:
            print("Se cancela la eliminación.")
    
    
    
    
    def salir(self):

        print("Gracias por utilizar el sistema.")
        sys.exit(0)

#Esta parte del código está fuera de la clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro módulo, sino ejecutado directamente), entonces llamamos al método
# ejecutar(). 
if __name__ == "__main__":
    m = Menu()
    m.ejecutar()
