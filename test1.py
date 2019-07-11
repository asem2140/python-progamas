class Persona:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def mostrarDatos(self):
  	print('Soy '+self.name+', mi edad es: '+str(self.age))
  	return 'hola'

persona1 = Persona("gus", 17)
# del persona1.age

print(persona1.mostrarDatos())
