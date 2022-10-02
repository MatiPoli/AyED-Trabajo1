#Integrantes:
#-Matías Marquez (107)
#-Alex Diaz (107)
#-Marcos Godoy (108)
#-Valentin Dalmau (108)

import os
import pickle
import os.path
import datetime
from datetime import date

class operaciones:
	def __init__(self):
		self.patente = " "
		self.codigo_producto = 0
		self.fecha_cupo = " "
		self.estado = " "
		self.bruto = 0
		self.tara = 0
class productos:
	def __init__(self):
		self.codigo = 0
		self.nombre = " "

class rubros:
	def __init__(self):
		self.codigo = 0
		self.nombre = " "

class rubros_x_producto:
	def __init__(self):
		self.codigo_rubro = 0
		self.codigo_producto = 0
		self.valor_minimo_admitido = 0.0
		self.valor_maximo_admitido = 0.0

class silos:
	def __init__(self):
		self.codigo_silo = 0
		self.nombre = " "
		self.codigo_producto = 0
		self.stock = 0


def formatearOperaciones(rOpera):
	rOpera.patente = rOpera.patente.ljust(7, ' ')
	rOpera.codigo_producto = str(rOpera.codigo_producto)
	rOpera.codigo_producto = rOpera.codigo_producto.ljust(5, ' ')
	rOpera.fecha_cupo = rOpera.fecha_cupo.ljust(15, ' ')
	rOpera.estado = rOpera.estado.ljust(1, ' ')
	rOpera.bruto = str(rOpera.bruto)
	rOpera.bruto = rOpera.bruto.ljust(10, ' ')
	rOpera.tara = str(rOpera.tara)
	rOpera.tara = rOpera.tara.ljust(10, ' ')

def formatearProductos(rProducto):
	rProducto.codigo = str(rProducto.codigo)
	rProducto.codigo = rProducto.codigo.ljust(5, ' ')
	rProducto.nombre = rProducto.nombre.ljust(15, ' ')

def formatearRubros(rRubro):
	rRubro.codigo = str(rRubro.codigo)
	rRubro.codigo = rRubro.codigo.ljust(5, ' ')
	rRubro.nombre = rRubro.nombre.ljust(15, ' ')

def formatearRubrosxProducto(rRxP):
	rRxP.codigo_rubro = str(rRxP.codigo_rubro)
	rRxP.codigo_rubro = rRxP.codigo_rubro.ljust(5, ' ')
	rRxP.codigo_producto = str(rRxP.codigo_producto)
	rRxP.codigo_producto = rRxP.codigo_producto.ljust(5, ' ')
	rRxP.valor_minimo_admitido = str(rRxP.valor_minimo_admitido)
	rRxP.valor_minimo_admitido = rRxP.valor_minimo_admitido.ljust(5, ' ')
	rRxP.valor_maximo_admitido = str(rRxP.valor_maximo_admitido)
	rRxP.valor_maximo_admitido = rRxP.valor_maximo_admitido.ljust(5, ' ')

def formatearSilos(rSilos):
	rSilos.codigo_silo = str(rSilos.codigo_silo)
	rSilos.codigo_silo = rSilos.codigo_silo.ljust(5, ' ')
	rSilos.nombre = rSilos.nombre.ljust(15, ' ')
	rSilos.codigo_producto = str(rSilos.codigo_producto)
	rSilos.codigo_producto = rSilos.codigo_producto.ljust(5, ' ')
	rSilos.stock = str(rSilos.stock)
	rSilos.stock = rSilos.stock.ljust(10, ' ')

def ordenaRubro():
	global ArcFisiRubro, ArcLogRubro
	ArcLogRubro.seek (0, 0)
	aux = pickle.load(ArcLogRubro)
	tamReg = ArcLogRubro.tell() 
	tamArch = os.path.getsize(ArcFisiRubro)
	cantReg = int(tamArch / tamReg)  
	for i in range(0, cantReg-1):
		for j in range (i+1, cantReg):
			ArcLogRubro.seek (i*tamReg, 0)
			auxi = pickle.load(ArcLogRubro)
			ArcLogRubro.seek (j*tamReg, 0)
			auxj = pickle.load(ArcLogRubro)
			if (int(auxi.codigo) > int(auxj.codigo)):
				ArcLogRubro.seek (i*tamReg, 0)
				pickle.dump(auxj, ArcLogRubro)
				ArcLogRubro.seek (j*tamReg, 0)
				pickle.dump(auxi, ArcLogRubro)
				ArcLogRubro.flush()

def ingresoInt(string):
	ban = 0
	while ban == 0:
		try:
			i = int(input(string))
			ban = 1
		except ValueError:
			print('Ingrese un numero correcto!\n')
	return i

def validarInt(num , min, max, string1, string2):
	while num < min or num > max:
		print(string1)
		num = ingresoInt(string2)
	return num

def validarString(string, min, max, string1, string2):
	while len(string) < min or len(string) > max:
		print(string1)
		string = str(input(string2).upper())
	return string

def buscaDico(num):
	global ArcFisiRubro, ArcLogRubro
	regRubro = rubros_x_producto()
	ArcLogRubro.seek (0, 0)
	aux = pickle.load(ArcLogRubro)
	tamReg = ArcLogRubro.tell() 
	cantReg = int(os.path.getsize(ArcFisiRubro) / tamReg)
	inferior = 0
	superior = cantReg-1
	medio = (inferior + superior) // 2 					
	ArcLogRubro.seek(medio*tamReg, 0)
	regRubro= pickle.load(ArcLogRubro) 					
	while int(regRubro.codigo)!= int(num) and (inferior < superior):
		if int(num) < int(regRubro.codigo):
			superior = medio - 1
		else:
			inferior = medio + 1
		medio = (inferior + superior) // 2 
		ArcLogRubro.seek(medio*tamReg, 0)
		regRubro = pickle.load(ArcLogRubro)
	
	ArcLogRubro.seek(medio*tamReg, 0)			
	regRubro= pickle.load(ArcLogRubro)
	return regRubro.nombre



# Caracteres: admin_option
def administraciones():
	admin_option = ''
	while admin_option != 'V':
		os.system('cls')
		print('MENU ADMINISTRACIONES')
		print('[A] Titulares')
		print('[B] Productos')
		print('[C] Rubros')
		print('[D] Rubros X Producto')
		print('[E] Silos')
		print('[F] Sucursales')
		print('[G] Rubros X Titular')
		print('[V] Volver al menu principal')
		admin_option: str = input('Opcion: ').upper()
		print('')
		if admin_option == 'A':
			menu('Titulares')
		elif admin_option == 'B':
			menu('Productos')
		elif admin_option == 'C':
			menu('Rubros')
		elif admin_option == 'D':
			menu('Rubros X Producto')
		elif admin_option == 'E':
			menu('Silos')
		elif admin_option == 'F':
			menu('Sucursales')
		elif admin_option == 'G':
			menu('Rubros X Titular')
		elif admin_option == 'V':
			print('')
		else:
			print('Opcion invalida!\n')
			os.system('pause')


# Enteros: i, ban, opcion
# Cadenas: type
# Caracteres: menu_option
def menu(type: str):
	global cant_productos

	global ArcLogProd, ArcFisiProd
	global ArcLogRubro, ArcFisiRubro
	global ArcLogRuXPro, ArcFisiRuXPro
	global ArcLogSilos, ArcFisiSilos

	menu_option = ''
	regProd = productos()
	regRubro = rubros()
	regRuXPro = rubros_x_producto()
	regSilos = silos()

	while menu_option != 'V':
		os.system('cls')
		print(f'MENU {type.upper()}')
		print('[A] Alta')
		print('[B] Baja')
		print('[C] Consulta')
		print('[M] Modificacion')
		print('[V] Volver al menu anterior')
		menu_option: str = input('Opcion: ').upper()
		print('')
		if type == "Titulares":
			print('Esta funcionalidad esta en construccion')
			os.system('pause')
		elif type == "Productos":
			if menu_option == 'A':
				ban = False
				tamArch = os.path.getsize(ArcFisiProd)
				puntero = tamArch
				ArcLogProd.seek(0,0)
				while ArcLogProd.tell() < tamArch and ban == False:
					pun = ArcLogProd.tell()
					regProd = pickle.load(ArcLogProd)
					puntero = ArcLogProd.tell()
					if int(regProd.codigo) == 0:
						ban = True
						puntero = pun
				regProd.codigo = ingresoInt('Ingrese el codigo:')
				while regProd.codigo <= 0 or regProd.codigo >= 100000:
					print('Codigo incorrecto!\n')
					regProd.codigo = ingresoInt('Ingrese el codigo:')

				regProd.nombre = str(input('\nIngrese el nombre: ').upper())
				while len(regProd.nombre) <= 0 or len(regProd.nombre) > 15:
					print('Largo del nombre incorrecto!\n')
					regProd.nombre = str(input('Ingrese el nombre: ').upper())
				formatearProductos(regProd)
				ArcLogProd.seek(puntero,0)
				pickle.dump(regProd, ArcLogProd)
				ArcLogProd.flush()
				#ban = 0
				#for i in range(3):
				#	if productos[i] == '' and ban != 1:
				#		ban = 1
				#		productos[i] = str(input('Ingrese el nombre del producto: ').upper())
				#if ban == 0:
				#	print('Se ha llenado la lista de productos, pruebe a modificarla.')
				#os.system('pause')
				print('')
				os.system('pause')
			elif menu_option == 'B':
				print('Listado de producto(s):')
				print('\nCodigo\tNombre')
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				while ArcLogProd.tell() < tamArch:
					regProd = pickle.load(ArcLogProd)
					print(str(regProd.codigo) + '\t' + regProd.nombre)
				cod = ingresoInt('\n¿Cual desea eliminar? Ingrese el codigo: ')
				while cod <= 0 or cod >= 100000:
					print('Codigo incorrecto!\n')
					cod = ingresoInt('\n¿Cual desea eliminar? Ingrese el codigo: ')

				ban = False
				ArcLogProd.seek(0,0)
				while ArcLogProd.tell() < tamArch and ban == False:
					puntero = ArcLogProd.tell()
					regProd = pickle.load(ArcLogProd)
					if int(regProd.codigo) == cod:
						ArcLogProd.seek(puntero,0)
						ban = True
						regProd.codigo = 0
						regProd.nombre = ' '
						formatearProductos(regProd)
						pickle.dump(regProd, ArcLogProd)
						ArcLogProd.flush()
				if ban == False:
					print('No se ha encontrado el producto!')
				print('')
				os.system('pause')
				"""
				print('Listado de producto(s):')
				for i in range(3):
					print(str(i) + ") " + productos[i])
				opcion = int(input('¿Cual desea eliminar? Ingrese el numero: '))
				if opcion >= 0 and opcion <= 2 and productos[opcion] != '':
					if cant_productos[opcion] == 0:
						productos[opcion] = ''
					else:
						print('No se puede eliminar esta opcion')
				else:
					print("Opcion invalida u opcion vacia!")
				os.system('pause')
				"""
			elif menu_option == 'C':
				print('Listado de producto(s):')
				print('\nCodigo\tNombre')
				print('------\t------')
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				while ArcLogProd.tell() < tamArch:
					regProd = pickle.load(ArcLogProd)
					if int(regProd.codigo) != 0:
						print(str(regProd.codigo) + '\t' + regProd.nombre)

				print('')
				os.system('pause')
				"""
				print('Listado de producto(s):')
				for i in range(3):
					print("- " + productos[i])
				os.system('pause')
				"""
			elif menu_option == 'M':
				print('Listado de producto(s):')
				print('\nCodigo\tNombre')
				print('------\t------')
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				while ArcLogProd.tell() < tamArch:
					regProd = pickle.load(ArcLogProd)
					print(str(regProd.codigo) + '\t' + regProd.nombre)


				cod = ingresoInt('\n¿Cual desea eliminar? Ingrese el codigo: ')
				while cod <= 0 or cod >= 100000:
					print('Codigo incorrecto!\n')
					cod = ingresoInt('¿Cual desea eliminar? Ingrese el codigo: ')

				ban = False
				ArcLogProd.seek(0,0)
				while ArcLogProd.tell() < tamArch and ban == False:
					puntero = ArcLogProd.tell()
					regProd = pickle.load(ArcLogProd)
					if int(regProd.codigo) == cod:
						ArcLogProd.seek(puntero,0)
						ban = True
						regProd.codigo = ingresoInt('Ingrese el codigo nuevo: ')
						while regProd.codigo <= 0 or regProd.codigo >= 100000:
							print('Codigo incorrecto!\n')
							regProd.codigo = ingresoInt('Ingrese el codigo nuevo:')
						regProd.nombre = str(input('\nIngrese el nombre nuevo: ').upper())
						while len(regProd.nombre) <= 0 or len(regProd.nombre) > 15:
							print('Largo del nombre incorrecto!\n')
							regProd.nombre = str(input('Ingrese el nombre nuevo: ').upper())
						formatearProductos(regProd)
						pickle.dump(regProd, ArcLogProd)
						ArcLogProd.flush()
				if ban == False:
					print('No se ha encontrado el producto!')
				print('')
				os.system('pause')
				"""
				print('Listado de producto(s):')
				for i in range(3):
					print(str(i) + ") " + productos[i])
				opcion = int(input('¿Cual desea modificar? Ingrese el numero: '))
				if opcion >= 0 and opcion <= 2 and productos[opcion] != '':
					productos[opcion] = str(input('Ingrese el nuevo nombre: ').upper())
				else:
					print("Opcion invalida u opcion vacia!")
				os.system('pause')
				"""
			elif menu_option == 'V':
				print('')
			else:
				print('Opcion invalida!\n')
				os.system('pause')
		elif type == "Rubros":
			if menu_option == 'A':
				ban = False
				ArcLogRubro.seek(0,0)
				tamArch = os.path.getsize(ArcFisiRubro)
				puntero = tamArch
				while ArcLogRubro.tell() < tamArch and ban == False:
					pun = ArcLogRubro.tell()
					regRubro = pickle.load(ArcLogRubro)
					puntero = ArcLogRubro.tell()
					if int(regRubro.codigo) == 0:
						ban = True
						pun = puntero
				regRubro.codigo = ingresoInt('Ingrese el codigo: ')
				while regRubro.codigo <= 0 or regRubro.codigo >= 100000:
					print('Codigo incorrecto!\n')
					regRubro.codigo = ingresoInt('Ingrese el codigo:')
				regRubro.nombre = str(input('\nIngrese el nombre: ').upper())
				while len(regRubro.nombre) <= 0 or len(regRubro.nombre) > 15:
					print('Largo del nombre incorrecto!\n')
					regRubro.nombre = str(input('Ingrese el nombre: ').upper())

				formatearRubros(regRubro)
				ArcLogRubro.seek(puntero,0)
				pickle.dump(regRubro, ArcLogRubro)
				ArcLogRubro.flush()
				ordenaRubro()
				print('')
				os.system('pause')

			elif menu_option == 'B':
				print('Esta funcionalidad esta en construccion')
				print('')
				os.system('pause')
			elif menu_option == 'C':
				print('Listado de rubro(s):')
				print('\nCodigo\tNombre')
				print('------\t------')
				ArcLogRubro.seek(0,0)
				tamArch = os.path.getsize(ArcFisiRubro)
				while ArcLogRubro.tell() < tamArch:
					regRubro = pickle.load(ArcLogRubro)
					if int(regRubro.codigo) != 0:
						print(str(regRubro.codigo) + '\t' + regRubro.nombre)
				print('')
				os.system('pause')
			elif menu_option == 'M':
				print('Esta funcionalidad esta en construccion')
				print('')
				os.system('pause')
			elif menu_option == 'V':
				print('')
			else:
				print('Opcion invalida!\n')
				os.system('pause')
		elif type == "Rubros X Producto":
			if menu_option == 'A':
				ban = False
				tamArch = os.path.getsize(ArcFisiRuXPro)
				puntero = tamArch
				ArcLogRuXPro.seek(0,0)
				while ArcLogRuXPro.tell() < tamArch and ban == False:
					pun = ArcLogRuXPro.tell()
					regRuXPro = pickle.load(ArcLogRuXPro)
					puntero = ArcLogRuXPro.tell()

					if int(regRuXPro.codigo_rubro) == 0:
						ban = True
						pun = puntero

				print('\nListado de producto(s):')
				print('\nCodigo\tNombre')
				print('------\t------')
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				while ArcLogProd.tell() < tamArch:
					regProd = pickle.load(ArcLogProd)
					print(str(regProd.codigo) + '\t' + regProd.nombre)
				ArcLogRubro.seek(0,0)
				ban = False
				while ban == False:
					cod = ingresoInt('\nIngrese el codigo del producto a asignar: ')
					cod = validarInt(cod,1,99999,"Codigo incorrecto!\n","\nIngrese el codigo del producto a asignar: ")

					ban = False
					tamArch = os.path.getsize(ArcFisiProd)
					ArcLogProd.seek(0,0)
					while ArcLogProd.tell() < tamArch and ban == False:
						regProd = pickle.load(ArcLogProd)
						if int(regProd.codigo) == cod:
							ban = True
							regRuXPro.codigo_producto = cod
					if ban == False:
						print('No se ha encontrado el producto!')

				print('\nListado de rubro(s):')
				print('\nCodigo\tNombre')
				print('------\t------')
				tamArch = os.path.getsize(ArcFisiRubro)
				while ArcLogRubro.tell() < tamArch:
					regRubro = pickle.load(ArcLogRubro)
					if int(regRubro.codigo) != 0:
						print(str(regRubro.codigo) + '\t' + regRubro.nombre)
				ban = False
				while ban == False:
					cod = ingresoInt('\nIngrese el codigo del rubro a asignar: ')
					cod = validarInt(cod,1,99999,"Codigo incorrecto!\n","\nIngrese el codigo del rubro a asignar: ")

					ban = False
					tamArch = os.path.getsize(ArcFisiRubro)
					ArcLogRubro.seek(0,0)
					while ArcLogRubro.tell() < tamArch and ban == False:
						regRubro = pickle.load(ArcLogRubro)
						if int(regRubro.codigo) == cod:
							ban = True
							regRuXPro.codigo_rubro = cod
					if ban == False:
						print('No se ha encontrado el producto!')


				regRuXPro.valor_minimo_admitido = ingresoInt('\nIngrese el valor minimo admitido: ')
				regRuXPro.valor_minimo_admitido = validarInt(regRuXPro.valor_minimo_admitido,0,99,'Minimo menor que 0 o mayor que 99!\n','Ingrese el valor minimo admitido: ')

				regRuXPro.valor_maximo_admitido = ingresoInt('\nIngrese el valor maximo admitido: ')
				while regRuXPro.valor_maximo_admitido > 100 and regRuXPro.valor_maximo_admitido > regRuXPro.valor_minimo_admitido:
					print('Maximo mayor que 100 o menor/igual que el valor minimo!\n')
					regRuXPro.valor_maximo_admitido = ingresoInt('Ingrese el valor valor maximo admitido: ')

				formatearRubrosxProducto(regRuXPro)
				ArcLogRuXPro.seek(puntero,0)
				pickle.dump(regRuXPro, ArcLogRuXPro)
				ArcLogRuXPro.flush()
				print('')
				os.system('pause')

			elif menu_option == 'B':
				print('Esta funcionalidad esta en construccion')
				print('')
				os.system('pause')
			elif menu_option == 'C':
				print('Listado de rubro(s) x producto(s):')
				print('\nCodigo\tCodigo\t\tValor\tValor')
				print('Rubro\tProducto\tMinimo\tMaximo')
				print('------\t--------\t------\t------')
				ArcLogRuXPro.seek(0,0)
				tamArch = os.path.getsize(ArcFisiRuXPro)
				while ArcLogRuXPro.tell() < tamArch:
					regRuXPro = pickle.load(ArcLogRuXPro)
					if int(regRuXPro.codigo_rubro) != 0:
						print(str(regRuXPro.codigo_rubro) + '\t' + str(regRuXPro.codigo_producto) + '\t\t' + str(regRuXPro.valor_minimo_admitido) + '\t' + str(regRuXPro.valor_maximo_admitido))

				print('')
				os.system('pause')
			elif menu_option == 'M':
				print('Esta funcionalidad esta en construccion')
				print('')
				os.system('pause')
			elif menu_option == 'V':
				print('')
			else:
				print('Opcion invalida!\n')
				os.system('pause')
		elif type == "Silos":
			if menu_option == 'A':
				ban = False
				tamArch = os.path.getsize(ArcFisiSilos)
				puntero = tamArch
				ArcLogSilos.seek(0,0)
				while ArcLogSilos.tell() < tamArch and ban == False:
					pun = ArcLogSilos.tell()
					regSilos = pickle.load(ArcLogSilos)
					puntero = ArcLogSilos.tell()
					if int(regSilos.codigo_silo) == 0:
						ban = True
						puntero = pun

				regSilos.codigo_silo = ingresoInt('Ingrese el codigo del silo: ')
				while regSilos.codigo_silo <= 0 or regSilos.codigo_silo >= 100000:
					print('Codigo incorrecto!\n')
					regSilos.codigo_silo = ingresoInt('Ingrese el codigo del silo:')

				regSilos.nombre = str(input('\nIngrese el nombre del silo: ').upper())
				while len(regSilos.nombre) <= 0 or len(regSilos.nombre) > 15:
					print('Largo del nombre incorrecto!\n')
					regSilos.nombre = str(input('Ingrese el nombre del silo: ').upper())

				regSilos.codigo_producto = ingresoInt('\nIngrese el codigo del producto: ')
				while regSilos.codigo_producto <= 0 or regSilos.codigo_producto >= 100000:
					print('Codigo incorrecto!\n')
					regSilos.codigo_producto = ingresoInt('Ingrese el codigo del producto:')

				formatearSilos(regSilos)
				ArcLogSilos.seek(puntero,0)
				pickle.dump(regSilos, ArcLogSilos)
				ArcLogSilos.flush()

			elif menu_option == 'B':
				print('Esta funcionalidad esta en construccion')
				print('')
				os.system('pause')
			elif menu_option == 'C':
				print('Listado de silo(s):')
				print('\nCodigo\tNombre\t\tCodigo\t\tStock')
				print('Silo\tSilo\t\tProducto')
				print('----\t------\t\t--------\t-----')
				ArcLogSilos.seek(0,0)
				tamArch = os.path.getsize(ArcFisiSilos)
				while ArcLogSilos.tell() < tamArch:
					regSilos = pickle.load(ArcLogSilos)
					if int(regSilos.codigo_silo) != 0:
						print(str(regSilos.codigo_silo) + '\t' + regSilos.nombre + '\t' + str(regSilos.codigo_producto) + '\t\t' + str(regSilos.stock))

				print('')
				os.system('pause')
			elif menu_option == 'M':
				print('Esta funcionalidad esta en construccion')
				print('')
				os.system('pause')
			elif menu_option == 'V':
				print('')
			else:
				print('Opcion invalida!\n')
				os.system('pause')
		elif type == "Sucursales":
			print('Esta funcionalidad esta en construccion')
			print('')
			os.system('pause')
		elif type == "Rubros X Titular":
			print('Esta funcionalidad esta en construccion')
			print('')
			os.system('pause')


# Enteros: ban, i, s, h, opcion
# Cadenas: opcion2
def entrega_de_cupos():
	
	global ArcLogProd, ArcFisiProd
	global ArcLogOpera, ArcFisiOpera

	regProd = productos()
	regOpera = operaciones()

	print("MENU ENTREGA DE CUPOS")
	print()
	patente = str(input("Ingrese la patente: ").upper())
	patente = validarString(patente,6,7,"Largo de la patente incorrecto!\n","\nIngrese la patente:")
	patente = patente.ljust(7, ' ')
	flag = True
	while flag:
		try:
			fecha = input("\nIngrese una fecha en formato dd/mm/aaaa: ")
			datetime.datetime.strptime(fecha, '%d/%m/%Y')
			flag = False
		except ValueError:
			print("Fecha invalida")
	fecha = fecha.ljust(15, ' ')
	tamArch = os.path.getsize(ArcFisiOpera)
	ban = False
	ArcLogOpera.seek(0,0)
	while ArcLogOpera.tell() < tamArch and ban == False:
		regOpera = pickle.load(ArcLogOpera)
		
		if regOpera.patente == patente and regOpera.fecha_cupo == fecha:
			print("La patente ingresada tiene un cupo asignado en esa fecha!")
			ban = True
	if ban == False:
		print('\nListado de producto(s):')
		print('\nCodigo\tNombre')
		print('------\t------')
		ArcLogProd.seek(0,0)
		tamArch = os.path.getsize(ArcFisiProd)
		while ArcLogProd.tell() < tamArch:
			regProd = pickle.load(ArcLogProd)
			print(str(regProd.codigo) + '\t' + regProd.nombre)
		cod = ingresoInt('\nIngrese el codigo del producto a asignar: ')
		cod = validarInt(cod,1,99999,"Codigo incorrecto!\n","\nIngrese el codigo del producto a asignar: ")

		ban = False
		tamArch = os.path.getsize(ArcFisiProd)
		ArcLogProd.seek(0,0)
		while ArcLogProd.tell() < tamArch and ban == False:
			regProd = pickle.load(ArcLogProd)
			if int(regProd.codigo) == cod:
				ban = True

				regOpera.patente = patente
				regOpera.codigo_producto = cod
				regOpera.fecha_cupo = fecha
				regOpera.estado = 'P'

				formatearOperaciones(regOpera)
				ArcLogOpera.seek(0,2)
				pickle.dump(regOpera, ArcLogOpera)
				ArcLogOpera.flush()
		if ban == False:
			print('No se ha encontrado el producto!')

	print()
	"""
	for s in range(3):
		if productos[s] != '':
			ban = 1
	if ban == 1:
		while opcion2 not in ['NO' , 'N']:
			ban = 0
			for i in range(8):
				if patentes[i] == '' and ban != 1:
					ban = 1
					patentes[i] = str(input('Ingrese la patente: ').upper())
					while len(patentes[i]) != 8 and len(patentes[i]) != 7:
						print('Largo de la patente incorrecto!')
						patentes[i] = str(input('Ingrese la patente: ').upper())

					for h in range(i):
						if patentes[i] == patentes[h]:
							print('Patente ya ingresada!')
							patentes[i] = ''
							opcion2 = 'N'


					if opcion2 != 'N':
						print('Listado de producto(s):')
						for s in range(3):
							print(str(s) + ") " + productos[s])
						opcion = int(input('¿Cual producto desea asignar? Ingrese el numero: '))
						while opcion < 0 or opcion > 2 or productos[opcion] == '':
							print("Opcion invalida u opcion vacia!")
							opcion = int(input('¿Cual producto desea asignar? Ingrese el numero: '))
						producto[i] = productos[opcion]
						cant_productos[opcion] = cant_productos[opcion] + 1
						cupones[i] = i + 1
						estado[i] = 'P'
						total_cupos = total_cupos + 1
			if ban == 0:
				print("Se ha alcanzado la entrega de cupos maxima diaria. Vuelva mañana!")
				opcion2 = 'N'
			else:
				opcion2: str = input('Desea ingresar otro cupo? (S/N): ').upper()
				while opcion2 not in ['YES', 'NO', 'N' , 'SI' , 'Y' , 'S']:
					print('Opcion incorrecta!')
					opcion2: str = input('Desea ingresar otro cupo? (S/N): ').upper()
				os.system('cls')
	else:
		print('No hay productos dados de alta!')
	"""


# Cadenas: buscar, opcion
# Enteros: ban, i
def recepcion():
	global ArcLogProd, ArcFisiProd
	global ArcLogOpera, ArcFisiOpera

	regProd = productos()
	regOpera = operaciones()
	opcion = ''
	while opcion not in ['NO' , 'N']:
		print("MENU RECEPCION")
		print()
		hoy = datetime.datetime.now().strftime('%d/%m/%Y')

		patente = str(input("Ingrese la patente: ").upper())
		patente = validarString(patente,6,7,"Largo de la patente incorrecto!\n","\nIngrese la patente: ")
		patente = patente.ljust(7,' ')
		hoy = hoy.ljust(15, ' ')

		tamArch = os.path.getsize(ArcFisiOpera)
		ban = False
		ArcLogOpera.seek(0,0)
		while ArcLogOpera.tell() < tamArch and ban == False:
			punt = ArcLogOpera.tell()
			regOpera = pickle.load(ArcLogOpera)

			if regOpera.patente == patente and regOpera.estado == 'P' and regOpera.fecha_cupo == hoy:
				regOpera.estado = 'A'
				ArcLogOpera.seek(punt, 0)

				formatearOperaciones(regOpera)
				pickle.dump(regOpera, ArcLogOpera)
				print("Camion arribado... \n")
				ArcLogOpera.flush()
				ban = True
		if ban == False:
			print("No se ha encontrado cupos para el dia de hoy!")
		opcion: str = input('Desea ingresar otro camion? (S/N): ').upper()
		while opcion not in ['YES', 'NO', 'N' , 'SI' , 'Y' , 'S']:
			print('Opcion incorrecta!')
			opcion: str = input('Desea ingresar otro camion? (S/N): ').upper()
		os.system('cls')

	"""
	opcion = ''
	while opcion not in ['NO' , 'N']:
		buscar = str(input('Ingrese la patente a buscar: ').upper())
		while len(buscar) != 8 and len(buscar) != 7:
			print('Largo de la patente incorrecto!')
			buscar = str(input('Ingrese la patente a buscar: ').upper())
		ban = 0
		for i in range(8):
			if patentes[i] == buscar:
				if estado[i] == 'P':
					estado[i] = 'E'
					total_camiones = total_camiones + 1
					ban = 1
					print('Se ha registrado la recepcion.')
				else:
					print('El estado de la patente solicitada no esta pendiente!')
		if ban == 0:
			print('No se ha encontrado la patente!')

		opcion: str = input('Desea ingresar otro camion? (S/N): ').upper()
		while opcion not in ['YES', 'NO', 'N' , 'SI' , 'Y' , 'S']:
			print('Opcion incorrecta!')
			opcion: str = input('Desea ingresar otro camion? (S/N): ').upper()
		os.system('cls')
	"""

def registrar_calidad():

	global ArcLogOpera, ArcFisiOpera
	global ArcLogRuXPro, ArcFisiRuXPro

	regOpera = operaciones()
	reguXPro = rubros_x_producto()

	print("MENU REGISTRAR CALIDAD")
	print()
	patente = str(input("Ingrese la patente: ").upper())
	patente = validarString(patente,6,7,"Largo de la patente incorrecto!\n","\nIngrese la patente:")
	patente = patente.ljust(7, ' ')

	tamArch = os.path.getsize(ArcFisiOpera)
	ban = False
	ArcLogOpera.seek(0,0)
	while ArcLogOpera.tell() < tamArch and ban == False:
		punt = ArcLogOpera.tell()
		regOpera = pickle.load(ArcLogOpera)
		
		if regOpera.patente == patente and regOpera.estado == 'A':
			ban = True
	if ban == True:
		ban = False
		mal = 0
		print('\nListado de rubros(s):')
		print('\nCodigo\tNombre')
		print('------\t--------')
		ArcLogRuXPro.seek(0,0)
		tamArch = os.path.getsize(ArcFisiRuXPro)
		while ArcLogRuXPro.tell() < tamArch:
			regRuXPro = pickle.load(ArcLogRuXPro)
			if regRuXPro.codigo_producto == regOpera.codigo_producto:
				nombre = buscaDico(regRuXPro.codigo_rubro)
				print()
				val = ingresoInt(str(regRuXPro.codigo_rubro) + '\t' + nombre + '\t\t' + "Valor registrado: ")
				while val < 0:
					print("Valor incorrecto!")
					val = ingresoInt(str(regRuXPro.codigo_rubro) + '\t' + nombre + '\t\t' + "Valor registrado: ")
				if val < int(regRuXPro.valor_minimo_admitido) or val > int(regRuXPro.valor_maximo_admitido):
					mal = mal + 1
				ban = True
		if ban == False:
			print('\nNo se han registrados rubros asignados al producto!')
		elif mal >= 2:
			print('\nNo se ha pasado el registro de calidad!')
			regOpera.estado = 'R'
			ArcLogOpera.seek(punt, 0)
			formatearOperaciones(regOpera)
			pickle.dump(regOpera, ArcLogOpera)
			ArcLogOpera.flush()
		else:
			print('\nSe ha pasado el registro de calidad!')
			regOpera.estado = 'C'
			ArcLogOpera.seek(punt, 0)
			formatearOperaciones(regOpera)
			pickle.dump(regOpera, ArcLogOpera)
			ArcLogOpera.flush()
	else:
		print("La patente ingresada no ha arribado o ya se ha registrado!\n")



# Cadenas: buscar
# Enteros: ban, i
def registrar_peso_bruto():
	global ArcLogOpera, ArcFisiOpera
	regOpera = operaciones()

	print("MENU REGISTRAR PESO BRUTO")
	print()
	patente = str(input("Ingrese la patente: ").upper())
	patente = validarString(patente,6,7,"Largo de la patente incorrecto!\n","\nIngrese la patente:")
	patente = patente.ljust(7, ' ')
	tamArch = os.path.getsize(ArcFisiOpera)
	ban = False
	ArcLogOpera.seek(0,0)
	while ArcLogOpera.tell() < tamArch and ban == False:

		punt = ArcLogOpera.tell()
		regOpera = pickle.load(ArcLogOpera)

		if regOpera.patente == patente and regOpera.estado == 'C':
			regOpera.estado = 'B' #cambio estado a bruto.

			pb = ingresoInt("\nIngrese el peso bruto:") #no se si esta bien asi
			while pb <= 0:
				print("Peso bruto incorrecto!")
				pb = ingresoInt("\n" + str(regRuXPro.codigo_rubro) + '\t' + nombre + '\t\t\t' + "Valor registrado: ")
			regOpera.bruto = pb

			ArcLogOpera.seek(punt,0)
			formatearOperaciones(regOpera)
			pickle.dump(regOpera, ArcLogOpera)
			print("Peso bruto asignado correctamente!\n")
			ArcLogOpera.flush()
			ban = True

	if ban == False:
		print("La patente ingresada no se ha aprobado o ya se ha registrado!\n")

	"""
	buscar = str(input('Ingrese la patente a buscar: ').upper())
	while len(buscar) != 8 and len(buscar) != 7:
		print('Largo de la patente incorrecto!')
		buscar = str(input('Ingrese la patente a buscar: ').upper())
	ban = 0
	for i in range(8):
		if patentes[i] == buscar:
			if estado[i] == 'E':
				if pesos_brutos[i] == 0:
					pesos_brutos[i] = int(input('Ingrese el peso bruto: '))
				else:
					print('La patente solicitada ya tiene un peso bruto asignada!')
			else:
				print('El estado de la patente solicitada no esta en proceso!')
			ban = 1
	if ban == 0:
		print('No se ha encontrado la patente!')
	"""

# Cadenas: buscar
# Enteros: ban, i
def registrar_tara():
	global ArcLogOpera, ArcFisiOpera
	global ArcLogSilos, ArcFisiSilos

	regOpera = operaciones()
	regSilos = silos()

	print("MENU REGISTRAR TARA")
	print()
	patente = str(input("Ingrese la patente: ").upper())
	patente = validarString(patente,6,7,"Largo de la patente incorrecto!\n","\nIngrese la patente:")
	patente = patente.ljust(7, ' ')
	tamArch = os.path.getsize(ArcFisiOpera)
	ban = False
	ban2 = False
	ArcLogOpera.seek(0,0)

	while ArcLogOpera.tell() < tamArch and ban == False:

		punt = ArcLogOpera.tell()
		regOpera = pickle.load(ArcLogOpera)

		if patente == regOpera.patente and regOpera.estado == 'B':
			#regOpera.estado == 'F'

			
			tara = ingresoInt("\nIngrese la tara: ") 
			while int(regOpera.bruto) < tara:
				print("La tara no puede ser menor al peso bruto!")
				tara = ingresoInt("\nIngrese la tara: ")
			
			peso_neto = int(regOpera.bruto) - tara
			ArcLogSilos.seek(0,0)
			tamArchS = os.path.getsize(ArcFisiSilos)

			while ArcLogSilos.tell() < tamArchS and ban == False:

				punt2 = ArcLogSilos.tell()
				regSilos = pickle.load(ArcLogSilos)
				if regOpera.codigo_producto == regSilos.codigo_producto:
					ban = True
					regSilos.stock = int(regSilos.stock) + peso_neto

					ArcLogSilos.seek(punt2,0) 
					formatearSilos(regSilos) # revisar formateo
					pickle.dump(regSilos, ArcLogSilos) #subo el nuevo registro
					ArcLogSilos.flush()

					regOpera.estado == 'F' #paso a finalizado
					ArcLogOpera.seek(punt,0)
					formatearOperaciones(regOpera)
					pickle.dump(regOpera, ArcLogOpera)
					ArcLogOpera.flush()
					print("Tara asignado correctamente!\n")

				ban2 = True
			ban = True
	if ban2 == False:
		print('No hay silos asignados a este producto!\n')

	"""
	buscar = str(input('Ingrese la patente a buscar: ').upper())
	while len(buscar) != 8 and len(buscar) != 7:
		print('Largo de la patente incorrecto!')
		buscar = str(input('Ingrese la patente a buscar: ').upper())
	ban = 0
	for i in range(8):
		if patentes[i] == buscar:
			if taras[i] == 0:
				if estado[i] == 'E':
					if pesos_brutos[i] != 0:
						taras[i] = int(input('Ingrese la tara: '))
						while taras[i] >= pesos_brutos[i]:
							print('La tara no puede ser mayor al peso bruto!')
							taras[i] = int(input('Ingrese la tara: '))
						for h in range(3):
							if producto[i] == productos[h]:
								peso_neto = pesos_brutos[i] - taras[i]
								pesos_netos_productos[h] = pesos_netos_productos[h] + peso_neto
								if mayor_menor_productos[h][0] == 0:
									patente_mm_productos[h][0] = patentes[i]
									mayor_menor_productos[h][0] = peso_neto
								elif peso_neto > mayor_menor_productos[h][0]:
									patente_mm_productos[h][0] = patentes[i]
									mayor_menor_productos[h][0] = peso_neto

								if mayor_menor_productos[h][1] == 0:
									patente_mm_productos[h][1] = patentes[i]
									mayor_menor_productos[h][1] = peso_neto
								elif peso_neto < mayor_menor_productos[h][1]:
									patente_mm_productos[h][1] = patentes[i]
									mayor_menor_productos[h][1] = peso_neto
					else:
						print('La patente solicitada no tiene un peso bruto asignada!')
				else:
					print('El estado de la patente solicitada no esta en proceso!')
			else:
				print('La patente solicitada tiene una tara asignada!')
			ban = 1
	if ban == 0:
		print('No se ha encontrado la patente!')
	"""

# Enteros: ban, i
# Reales: promedio
def reportes():
	global total_cupos
	global total_camiones
	global cant_productos
	global pesos_netos_productos
	global patente_mm_productos

	global producto 
	global patentes
	global pesos_brutos
	global taras


	"""
	os.system('cls')
	print('REPORTES\n')
	print(f'Cantidad total de cupos otorgados: {total_cupos}')
	print(f'Cantidad total de camiones recibidos: {total_camiones}')
	print('\nProducto(s):')
	ban = 0
	for i in range(3):
		if productos[i] != '':
			ban = 1
			print(f'--{productos[i]}--')
			print(f'Cantidad de total de camiones: {cant_productos[i]}')
			print(f'Peso neto total: {pesos_netos_productos[i]}')
			if cant_productos[i] == 0:
				promedio = 0
			else:
				promedio = pesos_netos_productos[i]/cant_productos[i]
			print(f'Promedio de peso neto por camion: {promedio:.2f}')
			print(f'Patente del camion que mas descargo: {patente_mm_productos[i][0]}')
			print(f'Patente del camion que menos descargo: {patente_mm_productos[i][1]}')
	if ban == 0:
		print('No se ha ingresado ningun producto!')
	ordenar_mostrar(producto[:],patentes[:],pesos_brutos[:],taras[:])
	"""

# Enteros: i, h, aux
# Char: aux
def listado_silos_rechazos():

	global ArcLogOpera, ArcFisiOpera
	global ArcLogSilos, ArcFisiSilos
	mayor = 0
	maxSilo = ''

	regOpera = operaciones()
	regSilos = silos()

	print("MENU LISTADO DE SILOS Y RECHAZOS")
	print()

	flag = True
	while flag:
		try:
			fecha = input("\nIngrese una fecha en formato dd/mm/aaaa: ")
			datetime.datetime.strptime(fecha, '%d/%m/%Y')
			flag = False
		except ValueError:
			print("Fecha invalida")
	fecha = fecha.ljust(15, ' ')

	ArcLogSilos.seek(0,0)
	tamArchS = os.path.getsize(ArcFisiSilos)

	while ArcLogSilos.tell() < tamArchS:

		regSilos = pickle.load(ArcLogSilos)
		if int(regSilos.stock) > mayor:
			maxSilo = regSilos.nombre
			mayor = int(regSilos.stock)

	print("\nEl silo con mayor stock fue: Silo " + maxSilo)
	print()

	ArcLogOpera.seek(0,0)
	tamArchO = os.path.getsize(ArcFisiOpera)
	ban = False
	print("Listado de camiones rechazados el dia " + fecha)
	while ArcLogOpera.tell() < tamArchO:

		regOpera = pickle.load(ArcLogOpera)
		if regOpera.fecha_cupo == fecha and regOpera.estado == 'R':
			ban = True
			print("- ", regOpera.patente)

	if ban == False:
		print("\nNo hay camiones rechazado en esta fecha!")
	print()
### Programa Principal ###

# TYPE
# ArrayEntero3 = array[1...3] of int
# ArrayEntero8 = array[1...8] of int
# ArrayCadena3 = array[1...3] of string
# ArrayCadena8 = array[1...8] of string
# BidEnteros = array[1...3, 1...2] of int
# BidCadenas = array[1...3, 1...2] of string

# VARIABLES
# ArrayEntero3: pesos_netos_productos, cant_productos
# ArrayEntero8: pesos_brutos, taras, cupones
# ArrayCadena3: productos
# ArrayCadena8: producto, patentes, estado
# BidEnteros: mayor_menor_productos
# BidCadenas: patente_mm_productos
# Enteros: total_cupos, total_camiones
# Chars: menu_option
def menu_principal():

	global ArcFisiOpera
	global ArcFisiProd
	global ArcFisiRubro
	global ArcFisiRuXPro
	global ArcFisiSilos

	ArcFisiOpera = "operaciones.dat"
	ArcFisiProd = "productos.dat"
	ArcFisiRubro = "rubros.dat"
	ArcFisiRuXPro = "rubros_x_producto.dat"
	ArcFisiSilos = "silos.dat"

	global ArcLogOpera
	global ArcLogProd
	global ArcLogRubro
	global ArcLogSilos
	global ArcLogRuXPro

	if not os.path.exists(ArcFisiOpera):
		ArcLogOpera = open(ArcFisiOpera, "w+b")
	else:
		ArcLogOpera = open(ArcFisiOpera, "r+b")

	if not os.path.exists(ArcFisiProd):
		ArcLogProd = open(ArcFisiProd, "w+b")
	else:
		ArcLogProd = open(ArcFisiProd, "r+b")

	if not os.path.exists(ArcFisiRubro):
		ArcLogRubro = open(ArcFisiRubro, "w+b")
	else:
		ArcLogRubro = open(ArcFisiRubro, "r+b")

	if not os.path.exists(ArcFisiRuXPro):
		ArcLogRuXPro = open(ArcFisiRuXPro, "w+b")
	else:
		ArcLogRuXPro = open(ArcFisiRuXPro, "r+b")

	if not os.path.exists(ArcFisiSilos):
		ArcLogSilos = open(ArcFisiSilos, "w+b")
	else:
		ArcLogSilos = open(ArcFisiSilos, "r+b")

	menu_option = '-1'
	while menu_option != '0':
		os.system('cls')
		print('MENU PRINCIPAL')
		print('[1] Administraciones')
		print('[2] Entrega de cupos')
		print('[3] Recepcion')
		print('[4] Registrar calidad')
		print('[5] Registrar peso bruto')
		print('[6] Registrar descarga')
		print('[7] Registrar tara')
		print('[8] Reportes')
		print('[9] Listado de silos y rechazos')
		print('[0] Salir')
		menu_option: str = input('Opcion: ')
		print('')
		if menu_option == '1':
			administraciones()
		elif menu_option == '2':
			os.system('cls')
			entrega_de_cupos()
			os.system('pause')
		elif menu_option == '3':
			os.system('cls')
			recepcion()
		elif menu_option == '4':
			os.system('cls')
			registrar_calidad()
			os.system('pause')
		elif menu_option == '5':
			os.system('cls')
			registrar_peso_bruto()
			os.system('pause')
		elif menu_option == '6':
			os.system('cls')
			print('Esta funcionalidad esta en construccion')
			os.system('pause')
		elif menu_option == '7':
			os.system('cls')
			registrar_tara()
			os.system('pause')
		elif menu_option == '8':
			os.system('cls')
			reportes()
			os.system('pause')
		elif menu_option == '9':
			os.system('cls')
			listado_silos_rechazos()
			os.system('pause')
		elif menu_option == '0':
			ArcLogOpera.close()
			ArcLogProd.close()
			ArcLogRubro.close()
			ArcLogSilos.close()
			ArcLogRuXPro.close()
			print('')
		else:
			print('Opcion invalida!\n')
			os.system('pause')


if __name__ == '__main__':
	menu_principal() #Este pedazo de código sirve para que un programa externo no pueda ejecutar este código