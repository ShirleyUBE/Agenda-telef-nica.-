class Contacto:
    def __init__(self, nombre, telefono, direccion, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class AgendaTelefonica:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        self.contactos = [contacto for contacto in self.contactos if contacto.nombre != nombre]

    def consultar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return vars(contacto)
        return "Contacto no encontrado."

    def mostrar_agenda(self):
        return [vars(contacto) for contacto in self.contactos]

# Uso de la agenda
agenda = AgendaTelefonica()
agenda.agregar_contacto(Contacto("Juan Pérez", "123456789", "Av. 9 de Octubre", "juan@correo.com"))
print(agenda.mostrar_agenda())
