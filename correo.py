from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class Correo:
	def __init__ (self, para):
		self.para = para

	def enviarEmail(self):
		#Crear una instancia de mensaje
		msg = MIMEMultipart()
		mensaje = "Usted ha ganado un 20% de descuento en todos nuestros productos. Aproveche la oferta!!!"

		#Establecemos los parámetros del correo
		password = "encuesta345"
		msg['De'] = "programacionencuesta@gmail.com"
		msg['Para'] = self.para
		msg['Subject'] = "OFERTA DE PRODUCTOS HIDRATANTES"

		#Agregar el cuerpo del mensaje
		msg.attach(MIMEText(mensaje, 'plain'))

		#Creamos el server
		server = smtplib.SMTP('smtp.gmail.com: 587')
		server.starttls()

		#Login
		server.login(msg['De'], password)

		#Enviamos el mensaje
		server.sendmail(msg['De'], msg['Para'], msg.as_string())
		server.quit()
		print(f'Se le envió un correo a {self.para}.\n')