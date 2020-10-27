from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioTrabajos import RepositorioTrabajos
from repositorioClientes import RepositorioClientes
from repositorio  import Repositorio
from trabajo import Trabajo



class ListaTrabajos:
    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.listatrabajo = self.rt.get_all()

    def nuevo_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, retirado, id_trabajo = None):
        t = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, retirado, id_trabajo = None)
        t.id_contacto = self.rt.store(t)
        if t.id_trabajo == 0:
            return None
        else:
            self.listatrabajo.append(t)
            return t

