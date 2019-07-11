# POO - Programación Orientada a Objetos
# Paradigma de programación mas cercado al mundo real (a diferencia de POP)
# Clases (Modelos/Plantilla) vs. Objetos (Instancias)
# Atributos (Características) y Métodos (Comportamiento)
# Instanciar - Crear objetos a partir de una clase
# Caso: Negocio de Bienestar y Salud bajo Multinivel - Nikken

# Clase de productos que comercializa la empresa
class Producto:
	# Método constructor - utilizado para iniciar los atributos
	def __init__(objeto, idProd, descripcion, precioMayor, precioVenta, stock):
		objeto.idProd = idProd
		objeto.descripcion = descripcion
		objeto.precioMayor = precioMayor
		objeto.precioVenta = precioVenta
		objeto.stock = stock
	# Método que actualiza el Stock
	def actStock(self, cantidad):
		if cantidad > 0:
			self.stock += cantidad
		elif cantidad < 0 and abs(cantidad) > self.stock:
			self.stock = 0
		return self.stock 

# Instancia e invoca métodos
wf = Producto("A101", "Waterfall", 1500, 1720, 10)
print(wf.idProd, wf.descripcion, wf.precioMayor, wf.precioVenta)
cant = 0
print(cant, wf.stock)
cant = 2
wf.actStock(cant)
print(cant, wf.stock)
cant = -20
wf.actStock(cant)
print(cant, wf.stock)
#
# pw = Producto("A102", "PiWater", 720, 400, 200)
# print(pw.idProd, pw.descripcion, pw.precioMayor, pw.precioVenta)
# cant = 0
# print(cant, wf.stock)
# cant = -5
# stk = pw.actStock(cant)
# print(cant, stk)
# cant = 10
# stk = pw.actStock(cant)
# print(cant, stk)