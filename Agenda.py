from datetime import date
from Contacto import Contacto
class Agenda:
  def __init__(self):
    self.__contactos = []
  
  @property
  def contactos(self):
    return self.__contactos
  
  
  def existeContacto(self, contacto):
    for cont in self.contactos:
      if cont.dni == contacto.dni:
        return True
    return False
  
  def agregarContacto(self, contacto):
    if self.existeContacto(contacto):
      print('El contacto ya existe') 
    else:
      self.contactos.append(contacto)
      
  def mostrarContactos(self):
    for i in self.contactos:
      print(i)

if __name__ == '__main__':
  agenda = Agenda()
  contacto1 = Contacto('Agustin', 'Carrizo', '38225312', 'agus@mail.com', '3834596585', date(1996,10,26), 'Figueroa Alcorta 1954')
  contacto2 = Contacto('Emanuel', 'Castro', '38285962', 'ema@mail.com', '383859631', date(1990,5,14), 'Corrientes 145')
  agenda.agregarContacto(contacto1)
  agenda.agregarContacto(contacto2)
  agenda.mostrarContactos()
  contacto3 = Contacto('Lautaro', 'Lopez', '38285962', 'lauti@mail.com', '12345678', date(2001,9,1), 'Corrientes 280')
  agenda.agregarContacto(contacto3)
  agenda.mostrarContactos()
  