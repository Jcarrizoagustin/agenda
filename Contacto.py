from datetime import date


class Contacto:
  contadorContactos = 0
  def __init__(self, nombre, apellido, dni, mail, telefono, fechaNacimiento, direccion):
    Contacto.contadorContactos += 1
    self.__nombre = nombre
    self.__apellido = apellido
    self.__dni = dni
    self.__mail = mail
    self.__telefono = telefono
    self.__fechaNacimiento = fechaNacimiento
    self.__direccion = direccion

  @property
  def nombre(self):
    return self.__nombre
  
  @nombre.setter
  def nombre(self, nombre):
    self.__nombre = nombre
  
  @property
  def apellido(self):
    return self.__apellido
  
  @apellido.setter
  def apellido(self, apellido):
    self.__apellido = apellido
  
  @property
  def dni(self):
    return self.__dni
  
  @dni.setter
  def dni(self, dni):
    self.__dni = dni
  
  @property
  def mail(self):
    return self.__mail
  
  @mail.setter
  def mail(self, mail):
    self.__mail = mail
  
  @property
  def telefono(self):
    return self.__telefono
  
  @telefono.setter
  def telefono(self, telefono):
    self.__telefono = telefono
  
  @property
  def fechaNacimiento(self):
    return self.__fechaNacimiento
  
  @fechaNacimiento.setter
  def fechaNacimiento(self, fechaNacimiento):
    self.__fechaNacimiento = fechaNacimiento
  
  @property
  def direccion(self):
    return self.__direccion
  
  @direccion.setter
  def direccion(self, direccion):
    self.__direccion = direccion
    
  def __str__(self):
    return f'''
      Nombre: {self.nombre}
      Apellido: {self.apellido}
      Dni: {self.dni}
      Mail: {self.mail}
      Telefono: {self.telefono}
      Fecha de Nacimiento: {self.fechaNacimiento}
      Direccion: {self.direccion}
  '''


if __name__ == '__main__':
  contacto = Contacto('Agustin', 'Carrizo', '38225312', 'agus@mail.com', '3834596585', date(1996,10,26), 'Figueroa Alcorta 1954')
  print(contacto)