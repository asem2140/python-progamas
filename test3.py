# POO - Programación Orientada a Objetos
# Paradigma de programación mas cercado al mundo real (a diferencia de POP)
# Clases (Modelos/Plantilla) vs. Objetos (Instancias)
# Atributos (Características) y Métodos (Comportamiento)
# Instanciar - Crear objetos a partir de una clase
# Caso: Negocio de Bienestar y Salud bajo Multinivel - Nikken

import math
import random

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
		if cantidad < 0 and abs(cantidad) > self.stock:
			self.stock = 0
		else:
			self.stock += cantidad
		return self.stock 

# Simula salida de producto hasta agotar stock
wf = Producto("A101", "Waterfall", 1500, 1720, 200)
print(wf.idProd, wf.descripcion, wf.precioMayor, wf.precioVenta)
cant = 0
print(cant, wf.stock)

# C/V de 1 a 10
while wf.stock > 0:
	x = -1*random.randint(1, 10)
	stk = wf.actStock(x)
	print(x, wf.stock)