#Integrantes:
#-Matías Marquez (107)
#-Bruno Zacchino (108)
#-Marcos Godoy (108)
#-Valentin Dalmau (108)

import os
import pickle
import os.path
import datetime
from datetime import date

class operaciones:
	def __init__(self):
		self.patente = ' '
		self.codigo_producto = 0
		self.fecha_cupo = ' '
		self.estado = ' '
		self.bruto = 0
		self.tara = 0

class productos:
	def __init__(self):
		self.codigo = 0
		self.nombre = ' '
		self.cant_camiones = 0
		self.neto = 0
		self.patente_menos = ' '
		self.cant_menos = 0

class rubros:
	def __init__(self):
		self.codigo = 0
		self.nombre = ' '

class rubros_x_producto:
	def __init__(self):
		self.codigo_rubro = 0
		self.codigo_producto = 0
		self.valor_minimo_admitido = 0.0
		self.valor_maximo_admitido = 0.0

class silos:
	def __init__(self):
		self.codigo_silo = 0
		self.nombre = ' '
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
	rProducto.cant_camiones = str(rProducto.cant_camiones)
	rProducto.cant_camiones = rProducto.cant_camiones.ljust(7, ' ')
	rProducto.neto = str(rProducto.neto)
	rProducto.neto = rProducto.neto.ljust(10, ' ')
	rProducto.patente_menos = rProducto.patente_menos.ljust(7, ' ')
	rProducto.cant_menos = str(rProducto.cant_menos)
	rProducto.cant_menos = rProducto.cant_menos.ljust(10, ' ')

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

def estaSilos(cod):
	global ArcLogSilos
	global ArcFisiSilos
	tamArch = os.path.getsize(ArcFisiSilos)
	ban = False
	regSilos = silos()
	ArcLogSilos.seek(0, 0)
	while ArcLogSilos.tell() < tamArch and ban == False:
		regSilos = pickle.load(ArcLogSilos)
		if int(regSilos.codigo_silo) == int(cod):
			return True
	return False

def estaSProd(cod):
	global ArcLogSilos
	global ArcFisiSilos
	tamArch = os.path.getsize(ArcFisiSilos)
	ban = False
	regSilos = silos()
	ArcLogSilos.seek(0, 0)
	while ArcLogSilos.tell() < tamArch and ban == False:
		regSilos = pickle.load(ArcLogSilos)
		if int(regSilos.codigo_producto) == int(cod):
			return True
	return False

def estaOProd(cod):
	global ArcLogOpera
	global ArcFisiOpera
	tamArch = os.path.getsize(ArcFisiOpera)
	ban = False
	regOpera = operaciones()
	ArcLogOpera.seek(0, 0)
	while ArcLogOpera.tell() < tamArch and ban == False:
		regOpera = pickle.load(ArcLogOpera)
		if int(regOpera.codigo_producto) == int(cod):
			return True
	return False

def estaProdRubro(cod):
	global ArcLogRuXPro
	global ArcFisiRuXPro
	tamArch = os.path.getsize(ArcFisiRuXPro)
	ban = False
	regRuXPro = rubros_x_producto()
	ArcLogRuXPro.seek(0, 0)
	while ArcLogRuXPro.tell() < tamArch and ban == False:
		regRuXPro = pickle.load(ArcLogRuXPro)
		if int(regRuXPro.codigo_producto) == int(cod) or int(regRuXPro.codigo_rubro) == int(cod):
			return True
	return False

def buscaProd(cod):
	global ArcLogProd, ArcFisiProd
	tamArch = os.path.getsize(ArcFisiProd)
	ArcLogProd.seek(0,0)
	regProd = productos()
	ban = False
	while ArcLogProd.tell() < tamArch and ban == False:
		punt = ArcLogProd.tell()
		regProd = pickle.load(ArcLogProd)
		if int(regProd.codigo) == int(cod):
			ban = True
	return punt

def buscaDico(num):
	global ArcFisiRubro, ArcLogRubro
	regRubro = rubros_x_producto()
	ArcLogRubro.seek(0, 0)
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
		if type == 'Titulares':
			if menu_option != 'V':
				print('Esta funcionalidad esta en construccion')
				print()
				os.system('pause')
		elif type == 'Productos':
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
				regProd.codigo = ingresoInt('Ingrese el codigo: ')
				regProd.codigo = validarInt(regProd.codigo,1,99999,'Codigo incorrecto!\n','Ingrese el codigo: ')

				regProd.nombre = str(input('\nIngrese el nombre: ').upper())
				regProd.nombre = validarString(regProd.nombre,1,15,'Largo del nombre incorrecto!\n','Ingrese el nombre: ')
				
				formatearProductos(regProd)
				ArcLogProd.seek(puntero,0)
				pickle.dump(regProd, ArcLogProd)
				ArcLogProd.flush()

				print()
				print('Alta hecha de forma exitosa!\n')
				os.system('pause')
			elif menu_option == 'B':
				print('Listado de producto(s):')
				print('\nCodigo\tNombre')
				print('------\t------')
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				if tamArch != 0:
					while ArcLogProd.tell() < tamArch:
						regProd = pickle.load(ArcLogProd)
						if int(regProd.codigo) != 0:
							print(str(regProd.codigo) + '\t' + regProd.nombre)
					cod = ingresoInt('\n¿Cual desea eliminar? Ingrese el codigo: ')
					cod = validarInt(cod,1,99999,'Codigo incorrecto!\n','\n¿Cual desea eliminar? Ingrese el codigo: ')

					if estaOProd(cod) != True or estaProdRubro(cod) != True:
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
								regProd.cant_camiones = 0
								regProd.neto = 0
								regProd.patente_menos = ' '
								regProd.cant_menos = 0
								formatearProductos(regProd)
								pickle.dump(regProd, ArcLogProd)
								ArcLogProd.flush()
								print('\nBorrado hecho de forma exitosa!')
						if ban == False:
							print('\nNo se ha encontrado el producto!')
					else:
						print('\nNo se puede borrar este producto!')
				else:
					print('\nNo hay productos dados de alta!')

				print()
				os.system('pause')
			elif menu_option == 'C':
				print('Listado de producto(s):')
				print('\nCodigo\tNombre')
				print('------\t------')
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				if tamArch != 0:
					while ArcLogProd.tell() < tamArch:
						punt = ArcLogProd.tell()
						regProd = pickle.load(ArcLogProd)
						if int(regProd.codigo) != 0:
							print(str(regProd.codigo) + '\t' + regProd.nombre )
				else:
					print('\nNo hay productos dados de alta!')

				print()
				os.system('pause')
			elif menu_option == 'M':
				print('Listado de producto(s):')
				print('\nCodigo\tNombre')
				print('------\t------')
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				if tamArch != 0:
					while ArcLogProd.tell() < tamArch:
						regProd = pickle.load(ArcLogProd)
						if int(regProd.codigo) != 0:
							print(str(regProd.codigo) + '\t' + regProd.nombre)

					cod = ingresoInt('\n¿Cual desea modificar? Ingrese el codigo: ')
					cod = validarInt(cod,1,99999,'Codigo incorrecto!\n','¿Cual desea modificar? Ingrese el codigo: ')
					
					ban = False
					ArcLogProd.seek(0,0)
					while ArcLogProd.tell() < tamArch and ban == False:
						puntero = ArcLogProd.tell()
						regProd = pickle.load(ArcLogProd)
						if int(regProd.codigo) == cod:
							ArcLogProd.seek(puntero,0)
							ban = True
							if estaOProd(regProd.codigo) == False:
								regProd.codigo = ingresoInt('Ingrese el codigo nuevo: ')
								regProd.codigo = validarInt(regProd.codigo,1,99999,'Codigo incorrecto!\n','Ingrese el codigo nuevo:')
							else:
								print('Ingrese el codigo nuevo: No se puede modificar el codigo!')
							
							regProd.nombre = str(input('\nIngrese el nombre nuevo: ').upper())
							regProd.nombre = validarIntl(regProd.nombre,1,15,'Largo del nombre incorrecto!\n','Ingrese el nombre nuevo: ')

							formatearProductos(regProd)
							pickle.dump(regProd, ArcLogProd)
							ArcLogProd.flush()
							print('\nModificacion hecha de forma exitosa!')
					if ban == False:
						print('\nNo se ha encontrado el producto!')
				else:
					print('\nNo hay productos dados de alta!')
				print()
				os.system('pause')
			elif menu_option == 'V':
				print()
			else:
				print('Opcion invalida!\n')
				os.system('pause')
		elif type == 'Rubros':
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
				regRubro.codigo = validarInt(regRubro.codigo,1,99999,'Codigo incorrecto!\n','Ingrese el codigo: ')

				regRubro.nombre = str(input('\nIngrese el nombre: ').upper())
				regRubro.nombre = validarString(regRubro.nombre,1,15,'Largo del nombre incorrecto!\n','Ingrese el nombre: ')

				formatearRubros(regRubro)
				ArcLogRubro.seek(puntero,0)
				pickle.dump(regRubro, ArcLogRubro)
				ArcLogRubro.flush()
				ordenaRubro()
				print()
				print('Alta hecha de forma exitosa!\n')
				os.system('pause')

			elif menu_option == 'B':
				print('Esta funcionalidad esta en construccion')
				print()
				os.system('pause')
			elif menu_option == 'C':
				print('Listado de rubro(s):')
				print('\nCodigo\tNombre')
				print('------\t------')
				ArcLogRubro.seek(0,0)
				tamArch = os.path.getsize(ArcFisiRubro)
				if tamArch != 0:
					while ArcLogRubro.tell() < tamArch:
						regRubro = pickle.load(ArcLogRubro)
						if int(regRubro.codigo) != 0:
							print(str(regRubro.codigo) + '\t' + regRubro.nombre)
				else:
					print('\nNo hay rubros dados de alta!')
				print()
				os.system('pause')
			elif menu_option == 'M':
				print('Esta funcionalidad esta en construccion')
				print()
				os.system('pause')
			elif menu_option == 'V':
				print()
			else:
				print('Opcion invalida!\n')
				os.system('pause')
		elif type == 'Rubros X Producto':
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

				if os.path.getsize(ArcFisiProd) != 0 and os.path.getsize(ArcFisiRubro) != 0:
					print('\nListado de producto(s):')
					print('\nCodigo\tNombre')
					print('------\t------')
					tamArch = os.path.getsize(ArcFisiProd)
					ArcLogProd.seek(0,0)
					while ArcLogProd.tell() < tamArch:
						regProd = pickle.load(ArcLogProd)
						if int(regProd.codigo) != 0:
							print(str(regProd.codigo) + '\t' + regProd.nombre)
					ArcLogRubro.seek(0,0)
					ban = False
					while ban == False:
						cod = ingresoInt('\nIngrese el codigo del producto a asignar: ')
						cod = validarInt(cod,1,99999,'Codigo incorrecto!\n','\nIngrese el codigo del producto a asignar: ')

						ban = False
						tamArch = os.path.getsize(ArcFisiProd)
						ArcLogProd.seek(0,0)
						while ArcLogProd.tell() < tamArch and ban == False:
							regProd = pickle.load(ArcLogProd)
							if int(regProd.codigo) == cod:
								ban = True
								regRuXPro.codigo_producto = cod
						if ban == False:
							print('\nNo se ha encontrado el producto!')

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
						cod = validarInt(cod,1,99999,'Codigo incorrecto!\n','\nIngrese el codigo del rubro a asignar: ')

						ban = False
						tamArch = os.path.getsize(ArcFisiRubro)
						ArcLogRubro.seek(0,0)
						while ArcLogRubro.tell() < tamArch and ban == False:
							regRubro = pickle.load(ArcLogRubro)
							if int(regRubro.codigo) == cod:
								ban = True
								regRuXPro.codigo_rubro = cod
						if ban == False:
							print('\nNo se ha encontrado el producto!')


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
					print('\nAlta hecha de forma exitosa!')
				else:
					print('\nNo hay productos o rubros dados de alta!')
				print()
				os.system('pause')

			elif menu_option == 'B':
				print('Esta funcionalidad esta en construccion')
				print()
				os.system('pause')
			elif menu_option == 'C':
				print('Listado de rubro(s) x producto(s):')
				print('\nCodigo\tCodigo\t\tValor\tValor')
				print('Rubro\tProducto\tMinimo\tMaximo')
				print('------\t--------\t------\t------')
				ArcLogRuXPro.seek(0,0)
				tamArch = os.path.getsize(ArcFisiRuXPro)
				if tamArch != 0:
					while ArcLogRuXPro.tell() < tamArch:
						regRuXPro = pickle.load(ArcLogRuXPro)
						if int(regRuXPro.codigo_rubro) != 0:
							print(str(regRuXPro.codigo_rubro) + '\t' + str(regRuXPro.codigo_producto) + '\t\t' + str(regRuXPro.valor_minimo_admitido) + '\t' + str(regRuXPro.valor_maximo_admitido))
				else:
					print('\nNo hay rubros x productos dados de alta!')
				print()
				os.system('pause')
			elif menu_option == 'M':
				print('Esta funcionalidad esta en construccion')
				print()
				os.system('pause')
			elif menu_option == 'V':
				print()
			else:
				print('Opcion invalida!\n')
				os.system('pause')
		elif type == 'Silos':
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

				if os.path.getsize(ArcFisiProd) != 0:
					regSilos.codigo_silo = ingresoInt('Ingrese el codigo del silo: ')
					regSilos.codigo_silo = validarInt(regSilos.codigo_silo,1,99999,'Codigo incorrecto!\n','Ingrese el codigo del silo: ')
					if estaSilos(regSilos.codigo_silo) == False:
						ArcLogSilos.seek(0,0)
						regSilos.nombre = str(input('\nIngrese el nombre del silo: ').upper())
						regSilos.nombre = validarString(regSilos.nombre,1,15,'Largo del nombre incorrecto!\n','Ingrese el nombre del silo: ')
							
						print('\nListado de producto(s):')
						print('\nCodigo\tNombre')
						print('------\t------')
						ArcLogProd.seek(0,0)
						tamArch = os.path.getsize(ArcFisiProd)
						if tamArch != 0:
							while ArcLogProd.tell() < tamArch:
								regProd = pickle.load(ArcLogProd)
								if int(regProd.codigo) != 0:
									print(str(regProd.codigo) + '\t' + regProd.nombre)
							ban2 = True
							cod = ingresoInt('\n¿Cual desea asignar? Ingrese el codigo: ')
							cod = validarInt(cod,1,99999,'Codigo incorrecto!\n','\n¿Cual desea asignar? Ingrese el codigo: ')

							ban = False
							ArcLogProd.seek(0,0)
							while ArcLogProd.tell() < tamArch and ban == False:
								regProd = pickle.load(ArcLogProd)
								if int(regProd.codigo) == cod:
									ban = True
							if ban == False:
								print('\nNo se ha encontrado el producto!\n')
							else:
								if estaSProd(cod) == False:
									regSilos.codigo_producto = cod
									formatearSilos(regSilos)
									ArcLogSilos.seek(puntero,0)
									pickle.dump(regSilos, ArcLogSilos)
									ArcLogSilos.flush()
									print('\nAlta hecha de forma exitosa!')
								else:
									print('\nEl producto ya tiene un silo asignado!')
						else:
							print('\nNo hay productos dados de alta!')
					else:
						print('\nCodigo ya ingresado!')
				else:
					print('\nNo hay productos dados de alta!')

				print()
				os.system('pause')		
			elif menu_option == 'B':
				print('Esta funcionalidad esta en construccion')
				print()
				os.system('pause')
			elif menu_option == 'C':
				print('Listado de silo(s):')
				print('\nCodigo\tNombre\t\tCodigo\t\tStock')
				print('Silo\tSilo\t\tProducto')
				print('----\t------\t\t--------\t-----')
				ArcLogSilos.seek(0,0)
				tamArch = os.path.getsize(ArcFisiSilos)
				if tamArch != 0:
					while ArcLogSilos.tell() < tamArch:
						regSilos = pickle.load(ArcLogSilos)
						if int(regSilos.codigo_silo) != 0:
							print(str(regSilos.codigo_silo) + '\t' + regSilos.nombre + '\t' + str(regSilos.codigo_producto) + '\t\t' + str(regSilos.stock))
				else:
					print('\nNo hay silos dados de alta!')
				print()
				os.system('pause')
			elif menu_option == 'M':
				print('Esta funcionalidad esta en construccion')
				print()
				os.system('pause')
			elif menu_option == 'V':
				print()
			else:
				print('Opcion invalida!\n')
				os.system('pause')
		elif type == 'Sucursales':
			if menu_option != 'V':
				print('Esta funcionalidad esta en construccion')
				print()
				os.system('pause')
				
		elif type == 'Rubros X Titular':
			if menu_option != 'V':
				print('Esta funcionalidad esta en construccion')
				print()
				os.system('pause')


def entrega_de_cupos():
	
	global ArcLogProd, ArcFisiProd
	global ArcLogOpera, ArcFisiOpera

	regProd = productos()
	regOpera = operaciones()

	print('MENU ENTREGA DE CUPOS')
	print()
	patente = str(input('Ingrese la patente: ').upper())
	patente = validarString(patente,6,7,'Largo de la patente incorrecto!\n','\nIngrese la patente: ')
	patente = patente.ljust(7, ' ')
	flag = True
	while flag:
		try:
			fecha = input('\nIngrese una fecha en formato dd/mm/aaaa: ')
			datetime.datetime.strptime(fecha, '%d/%m/%Y')
			flag = False
		except ValueError:
			print('Fecha invalida')
	fecha = fecha.ljust(15, ' ')
	tamArch = os.path.getsize(ArcFisiOpera)
	ban = False
	ArcLogOpera.seek(0,0)
	while ArcLogOpera.tell() < tamArch and ban == False:
		regOpera = pickle.load(ArcLogOpera)
		
		if regOpera.patente == patente and regOpera.fecha_cupo == fecha:
			print('La patente ingresada tiene un cupo asignado en esa fecha!')
			ban = True
	if ban == False:
		print('\nListado de producto(s):')
		print('\nCodigo\tNombre')
		print('------\t------')
		ArcLogProd.seek(0,0)
		tamArch = os.path.getsize(ArcFisiProd)
		while ArcLogProd.tell() < tamArch:
			regProd = pickle.load(ArcLogProd)
			if int(regProd.codigo) != 0:
				print(str(regProd.codigo) + '\t' + regProd.nombre)
		cod = ingresoInt('\nIngrese el codigo del producto a asignar: ')
		cod = validarInt(cod,1,99999,'Codigo incorrecto!\n','\nIngrese el codigo del producto a asignar: ')

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
				print('\nCupo entregado de forma exitosa!')
		if ban == False:
			print('\nNo se ha encontrado el producto!')

	print()

def recepcion():
	global ArcLogProd, ArcFisiProd
	global ArcLogOpera, ArcFisiOpera

	regProd = productos()
	regOpera = operaciones()
	opcion = ''
	while opcion not in ['NO' , 'N']:
		print('MENU RECEPCION')
		print()
		hoy = datetime.datetime.now().strftime('%d/%m/%Y')

		patente = str(input('Ingrese la patente: ').upper())
		patente = validarString(patente,6,7,'Largo de la patente incorrecto!\n','\nIngrese la patente: ')
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
				print('\nCamion arribado... \n')
				ArcLogOpera.flush()
				ban = True
		if ban == False:
			print('\nNo se han encontrado cupos para el dia de hoy!\n')
		opcion: str = input('Desea ingresar otro camion? (S/N): ').upper()
		while opcion not in ['YES', 'NO', 'N' , 'SI' , 'Y' , 'S']:
			print('Opcion incorrecta!')
			opcion: str = input('Desea ingresar otro camion? (S/N): ').upper()
		os.system('cls')


def registrar_calidad():

	global ArcLogOpera, ArcFisiOpera
	global ArcLogRuXPro, ArcFisiRuXPro

	regOpera = operaciones()
	reguXPro = rubros_x_producto()

	print('MENU REGISTRAR CALIDAD')
	print()
	patente = str(input('Ingrese la patente: ').upper())
	patente = validarString(patente,6,7,'Largo de la patente incorrecto!\n','\nIngrese la patente:')
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
				val = ingresoInt(str(regRuXPro.codigo_rubro) + '\t' + nombre + '\t\t' + 'Valor registrado: ')
				while val < 0:
					print('Valor incorrecto!')
					val = ingresoInt(str(regRuXPro.codigo_rubro) + '\t' + nombre + '\t\t' + 'Valor registrado: ')
				if val < int(regRuXPro.valor_minimo_admitido) or val > int(regRuXPro.valor_maximo_admitido):
					mal = mal + 1
				ban = True
		if ban == False:
			print('\nNo se han registrados rubros asignados al producto!')
		elif mal >= 2:
			print('\nNo se ha pasado el registro de calidad!\n')
			regOpera.estado = 'R'
			ArcLogOpera.seek(punt, 0)
			formatearOperaciones(regOpera)
			pickle.dump(regOpera, ArcLogOpera)
			ArcLogOpera.flush()
		else:
			print('\nSe ha pasado el registro de calidad!\n')
			regOpera.estado = 'C'
			ArcLogOpera.seek(punt, 0)
			formatearOperaciones(regOpera)
			pickle.dump(regOpera, ArcLogOpera)
			ArcLogOpera.flush()
	else:
		print('\nLa patente ingresada no ha arribado o ya se ha registrado!\n')



def registrar_peso_bruto():
	global ArcLogOpera, ArcFisiOpera
	regOpera = operaciones()

	print('MENU REGISTRAR PESO BRUTO')
	print()
	patente = str(input('Ingrese la patente: ').upper())
	patente = validarString(patente,6,7,'Largo de la patente incorrecto!\n','\nIngrese la patente:')
	patente = patente.ljust(7, ' ')
	tamArch = os.path.getsize(ArcFisiOpera)
	ban = False
	ArcLogOpera.seek(0,0)
	while ArcLogOpera.tell() < tamArch and ban == False:

		punt = ArcLogOpera.tell()
		regOpera = pickle.load(ArcLogOpera)

		if regOpera.patente == patente and regOpera.estado == 'C':
			regOpera.estado = 'B' #cambio estado a bruto.

			pb = ingresoInt('\nIngrese el peso bruto: ')
			while pb <= 0:
				print('Peso bruto incorrecto!')
				pb = ingresoInt('\nIngrese el peso bruto: ')
			regOpera.bruto = pb

			ArcLogOpera.seek(punt,0)
			formatearOperaciones(regOpera)
			pickle.dump(regOpera, ArcLogOpera)
			print('\nPeso bruto asignado correctamente!\n')
			ArcLogOpera.flush()
			ban = True

	if ban == False:
		print('\nLa patente ingresada no se ha aprobado o ya se ha registrado!\n')


def registrar_tara():
	global ArcLogOpera, ArcFisiOpera
	global ArcLogSilos, ArcFisiSilos
	global ArcLogProd, ArcFisiProd

	regOpera = operaciones()
	regSilos = silos()
	regProd = productos()

	print('MENU REGISTRAR TARA')
	print()
	patente = str(input('Ingrese la patente: ').upper())
	patente = validarString(patente,6,7,'Largo de la patente incorrecto!\n','\nIngrese la patente:')
	patente = patente.ljust(7, ' ')
	tamArch = os.path.getsize(ArcFisiOpera)
	ban = False
	ban2 = False
	ArcLogOpera.seek(0,0)
	while ArcLogOpera.tell() < tamArch and ban == False:

		punt = ArcLogOpera.tell()
		regOpera = pickle.load(ArcLogOpera)
		
		if patente == regOpera.patente and regOpera.estado == 'B':		
			tara = ingresoInt('\nIngrese la tara: ') 
			while int(regOpera.bruto) < tara:
				print('La tara no puede ser menor al peso bruto!')
				tara = ingresoInt('\nIngrese la tara: ')
			
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

					cod = regOpera.codigo_producto
					neto = int(regOpera.bruto) - tara
					patente2 = regOpera.patente
					regOpera.tara = tara
					regOpera.estado = 'F' #paso a finalizado
					ArcLogOpera.seek(punt,0)
					formatearOperaciones(regOpera)
					pickle.dump(regOpera, ArcLogOpera)
					ArcLogOpera.flush()

					ArcLogProd.seek(buscaProd(cod),0)
					regProd = pickle.load(ArcLogProd)
					ArcLogProd.seek(buscaProd(cod),0)
					regProd.cant_camiones = int(regProd.cant_camiones) + 1
					regProd.neto = int(regProd.neto) + neto
					if int(regProd.cant_menos) == 0 or int(regProd.cant_menos) > neto:
						regProd.cant_menos = neto
						regProd.patente_menos = patente2
					formatearProductos(regProd)
					pickle.dump(regProd, ArcLogProd)
					ArcLogProd.flush()

					print('\nTara asignada correctamente!\n')

				ban2 = True
			ban = True
	if ban == False:
		print('\nLa patente no tiene peso bruto registrado o ya se ha ingresado la tara!\n')
	elif ban2 == False:
		print('\nNo hay silos asignados a este producto!\n')



def contenido(x, M):
	i = 0 
	ban = False
	while M[i][0] != 0 and ban == False:
		if M[i][0] == x:
			ban = True
	return ban


def reportes():
	global ArcLogOpera, ArcFisiOpera
	global ArcLogSilos, ArcFisiSilos
	global ArcLogProd, ArcFisiProd

	regProd = productos()
	regOpera = operaciones()
	regSilos = silos()
	recibidos = 0

	print('MENU REPORTES')
	print()

	ArcLogOpera.seek(0,0)
	tamArchO = os.path.getsize(ArcFisiOpera)
	if tamArchO != 0:
		regOpera = pickle.load(ArcLogOpera)
		tamReg = ArcLogOpera.tell() # saca el tamaño del registro
		cantReg = tamArchO//tamReg # saco cant de registros q es igual a la cant de cupos
		print('-Cantidad de cupos otorgados: ', cantReg)

		#2
		ArcLogOpera.seek(0,0)
		while ArcLogOpera.tell() < tamArchO:
			regOpera = pickle.load(ArcLogOpera)
			if regOpera.estado == 'F':
				recibidos = recibidos + 1
		print('\n-Cantidad de camiones recibidos: ', recibidos)

		print('\nProducto(s):')
		if os.path.getsize(ArcFisiProd) != 0:
			ArcLogProd.seek(0,0)
			tamArchP = os.path.getsize(ArcFisiProd)
			while ArcLogProd.tell() < tamArchP:
				regProd = pickle.load(ArcLogProd)
				if int(regProd.codigo) != 0:
					print(f'\n--{regProd.nombre.rstrip()}--')
					print('Cantidad de total de camiones: ' + str(regProd.cant_camiones))	
					print(f'Peso neto total: ' + str(regProd.neto))
					if int(regProd.cant_camiones) == 0:
						promedio = 0
					else:
						promedio = int(regProd.neto)/int(regProd.cant_camiones)
					print(f'Promedio de peso neto por camion: {promedio:.2f}')
					print(f'Patente del camion que menos descargo: {regProd.patente_menos}')

		else:
			print('\nNo hay productos dados de alta!')
	else:
		print('\nNo se han hecho operaciones!\n')
	print()



def listado_silos_rechazos():

	global ArcLogOpera, ArcFisiOpera
	global ArcLogSilos, ArcFisiSilos
	mayor = 0
	maxSilo = ''

	regOpera = operaciones()
	regSilos = silos()

	print('MENU LISTADO DE SILOS Y RECHAZOS')
	print()

	ArcLogSilos.seek(0,0)
	tamArchS = os.path.getsize(ArcFisiSilos)
	if tamArchS != 0:
		while ArcLogSilos.tell() < tamArchS:

			regSilos = pickle.load(ArcLogSilos)
			if int(regSilos.stock) > mayor:
				maxSilo = regSilos.nombre
				mayor = int(regSilos.stock)

		print('El silo con mayor stock fue: Silo ' + maxSilo)
		print()
	else:
		print('El silo con mayor stock fue: ---- ')
		print()
	flag = True
	while flag:
		try:
			fecha = input('Ingrese una fecha en formato dd/mm/aaaa: ')
			datetime.datetime.strptime(fecha, '%d/%m/%Y')
			flag = False
		except ValueError:
			print('Fecha invalida')
	fecha = fecha.ljust(15, ' ')
	ArcLogOpera.seek(0,0)
	tamArchO = os.path.getsize(ArcFisiOpera)
	ban = False
	print('\nListado de camiones rechazados el dia ' + fecha)
	if tamArchO != 0:
		while ArcLogOpera.tell() < tamArchO:

			regOpera = pickle.load(ArcLogOpera)
			if regOpera.fecha_cupo == fecha and regOpera.estado == 'R':
				ban = True
				print('- ', regOpera.patente)

		if ban == False:
			print('\nNo hay camiones rechazado en esta fecha!')
		print()
	else:
		print('\nNo se han hecho operaciones!\n')

### Programa Principal ###
def menu_principal():

	global ArcFisiOpera
	global ArcFisiProd
	global ArcFisiRubro
	global ArcFisiRuXPro
	global ArcFisiSilos

	ArcFisiOpera = 'operaciones.dat'
	ArcFisiProd = 'productos.dat'
	ArcFisiRubro = 'rubros.dat'
	ArcFisiRuXPro = 'rubros_x_producto.dat'
	ArcFisiSilos = 'silos.dat'

	global ArcLogOpera
	global ArcLogProd
	global ArcLogRubro
	global ArcLogSilos
	global ArcLogRuXPro

	if not os.path.exists(ArcFisiOpera):
		ArcLogOpera = open(ArcFisiOpera, 'w+b')
	else:
		ArcLogOpera = open(ArcFisiOpera, 'r+b')

	if not os.path.exists(ArcFisiProd):
		ArcLogProd = open(ArcFisiProd, 'w+b')
	else:
		ArcLogProd = open(ArcFisiProd, 'r+b')

	if not os.path.exists(ArcFisiRubro):
		ArcLogRubro = open(ArcFisiRubro, 'w+b')
	else:
		ArcLogRubro = open(ArcFisiRubro, 'r+b')

	if not os.path.exists(ArcFisiRuXPro):
		ArcLogRuXPro = open(ArcFisiRuXPro, 'w+b')
	else:
		ArcLogRuXPro = open(ArcFisiRuXPro, 'r+b')

	if not os.path.exists(ArcFisiSilos):
		ArcLogSilos = open(ArcFisiSilos, 'w+b')
	else:
		ArcLogSilos = open(ArcFisiSilos, 'r+b')

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