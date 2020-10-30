#! /usr/bin/env python3
import sys
from listaClientes import ListaClientes
from repositorioTrabajos import RepositorioTrabajos
from repositorioClientes import RepositorioClientes
from repositorio import Repositorio
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from listaTrabajos import ListaTrabajos
from datetime import datetime 
from datetime import date
from trabajo import Trabajo
from tkinter import ttk
from tkinter import *




class Menu:
    '''Mostrar un menú y responder a las opciones'''
    def __init__(self):
        self.repotrabajo = RepositorioTrabajos()
        self.lista_clientes = ListaClientes()
        self.recl = RepositorioClientes()
        self.repo = Repositorio()
        self.listaT = ListaTrabajos()
        self.opciones= {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.actualizar_datos,
            "4": self.eliminar_cliente,
            "5": self.nuevo_trabajo,
            "6": self.mostrar_trabajo,
            "7": self.modificar_trabajo,
            "8": self.eliminar_trabajo,
            "9": self.generar_informe,
            "0": self.salir
        }

    def mostrar_menu(self):
        print("""
Menú del anotador:
1.  Mostrar todos los clientes 
2.  Ingresar los datos del nuevo cliente 
3.  Actualizar datos de un cliente 
4.  Eliminar cliente 
5.  Ingresar los datos del nuevo trabajo 
6.  Mostrar trabajos 
7.  Modificar datos de trabajo (registro de trabajo retirado/finalizado)  
8.  Eliminar trabajo 
9.  Generar informe
0.  Salir 
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
            c = self.lista_clientes.nuevo_cliente_corporativo(nombre, contacto, tc, tel, mail)
        else:
            c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido, tel, mail)
        if c is None:
            print("Error al cargar el trabajo")
        else:
            print("Trabajo cargado correctamente")



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
    

    def nuevo_trabajo(self):
        id_cliente = int(input("Ingrese ID del cliente al que le desea asignar un trabajo: "))
        ingreso_trabajo = input("Ingrese N para ingresar un trabajo al cliente: ")
        cliente = self.recl.get_one(id_cliente)
        if ingreso_trabajo in ("N", "n"):
            hoy = datetime.today()
            ingreso = hoy
            dia = int(input("Ingrese el dia propuesto para la entrega: "))
            mes = int(input("Ingrese el mes propuesto para la entrega (en número, 1 a 12): "))
            anio = int(input("Ingrese el año propuesto para la entrega (4 dígitos): "))
            fecha_entrega_propuesta = datetime(anio, mes, dia)
            fecha_entrega_real = None
            descripcion = input("Ingrese una breve descripcion del trabajo: ")
            retirado = False
            t = self.listaT.nuevo_trabajo(cliente, ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, retirado)
            if t == 0:
                print("Error al cargar el cliente. ")
            else:
                print("Cliente cargado correctamente!")
        else: 
            if ingreso_trabajo != ("N", "n"):
                print("Ingreso de trabajo CANCELADO. ")

    def mostrar_trabajo(self, listaT = None):
        if listaT == None:
            listaT = self.listaT.listatrabajo
        for Trabajo in listaT:
            print(Trabajo)

    def modificar_trabajo(self):
        id_trabajo = int(input("Ingrese ID de trabajo al que le desea modificar un trabajo: "))
        mod_trabajo= input("Ingrese M para modificar un trabajo al cliente: ")
        trabajo = self.repotrabajo.get_one(id_trabajo)
        if mod_trabajo in ("M", "m"):
            mod_descripcion = input("Si desea modificar la descripcion presione X, si no presione otra letra: ")
            if mod_descripcion in ("X","x"):
                descripcion = input("Ingrese una breve descripcion del trabajo: ")
                trabajo.descripcion = descripcion
                mod_ingreso = input("Si desea modificar la fecha de ingreso presione X, si no presione otra letra: ")
                if mod_ingreso in ("X","x"):
                    hoy = datetime.today()
                    ingreso = hoy
                    trabajo.ingreso = ingreso
                    print("Se modifico la descripcion y la fecha de ingreso ! ")
                else:
                    print("Se modifico solamente la descripcion")
            else:
                mod_ingreso = input("Si desea modificar la fecha de ingreso presione X, si no presione otra letra: ")
                if mod_ingreso in ("X","x"):
                    hoy = datetime.today()
                    ingreso = hoy
                    trabajo.ingreso = ingreso
                    print("Se modifico la fecha de ingreso !")
                else:
                    print("No se modificó la fecha de entrega. ")
            mod_fechapropuesta = input("Si desea modificar la fecha propuesta presione X, si no presione otra letra: ")
            if mod_fechapropuesta in ("X", "x"):
                dia = int(input("Ingrese el dia propuesto para la entrega: "))
                mes = int(input("Ingrese el mes propuesto para la entrega (en número, 1 a 12): "))
                anio = int(input("Ingrese el año propuesto para la entrega (4 dígitos): "))
                fecha_entrega_propuesta = datetime(anio, mes, dia)
                trabajo.fecha_entrega_propuesta = fecha_entrega_propuesta
                print("Se modificó la fecha propuesta de entrega !")
            else:
                print("No se modifico la fecha propuesta de entrega")
            mod_fechareal = input("Ingrese X para modificar la fecha de entrega real, si no presione otra letra: ")
            if mod_fechareal in ("X", "x"):
                hoy = datetime.today()
                fecha_entrega_real = hoy
                trabajo.fecha_entrega_real = fecha_entrega_real
                print("Se modificó la fecha de entrega real. ")
            else:
                print("No se modificó la fecha de entrega real")
            mod_retirado = input("Ingrese X para modificar si el trabajo fue retirado, si no fue retirado presione N, si no presione otra letra: ")
            if mod_retirado in ("X", "x"):
                retirado = True
                trabajo.retirado = retirado
                print("El trabajó fue retirado.")
                t = self.repotrabajo.update(trabajo)                
            else:
                if mod_retirado in ("N", "n"):
                    print("El trabajo no fue retirado")
                    retirado = False  
                    trabajo.retirado = retirado
                    t = self.repotrabajo.update(trabajo)
            print("Datos actualizados correctamente !")
            t = self.repotrabajo.update(trabajo)



    def eliminar_trabajo(self):
        id_trabajo = int(input("Ingrese ID de trabajo del cliente para eliminar sus trabajos: "))
        borrar = input("Para eliminar los datos del cliente ingrese E, de caso contrario se cancelará la eliminación: ")
        trabajo = self.repotrabajo.get_one(id_trabajo)
        if borrar == "E" or "e":
            t = self.repotrabajo.delete(trabajo)
            if t == 0:
                print("El trabajo ha sido eliminado")
            else:
                print("No se eliminó correctamente")
            print("Eliminación del trabajo de manera exitosa.")
        else:
            print("Se cancela la eliminación.")



    def generar_informe(self, listatrabajo = None):
        id_cliente = int(input("Ingrese ID del cliente para ver un informe de sus trabajos encargados: "))
        gen_inf = input("Para generar un informe de los trabajos presione X: ")
        cliente = self.recl.get_one(id_cliente)
        id_trabajo = ""
        listaT = self.repotrabajo.get_one(id_trabajo)
        t = self.listaT.un_trabajo
        if gen_inf in ("X", "x"):
            print(cliente)
            print(listaT)
            print(t)
 
        else:
            print("No se genero ningún informe. ")
    

    
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
