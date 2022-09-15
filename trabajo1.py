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
			print('Opcion invalida!')
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
		if type == "Titulares":
			print('Esta funcionalidad esta en construccion')
			os.system('pause')
		elif type == "Productos":
			if menu_option == 'A':
				regProd.codigo = int(input('Ingrese el codigo: '))
				while regProd.codigo <= 0 or regProd.codigo >= 100000:
					print('Codigo incorrecto!')
					regProd.codigo = int(input('Ingrese el codigo:'))
				regProd.nombre = str(input('\nIngrese el nombre: ').upper())
				while len(regProd.nombre) <= 0 or len(regProd.nombre) > 15:
					print('Largo del nombre incorrecto!')
					regProd.nombre = str(input('Ingrese el nombre: ').upper())
				formatearProductos(regProd)
				ArcLogProd.seek(0,2)
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
			elif menu_option == 'B':
				print('Listado de producto(s):')
				print('\nCodigo\tNombre')
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				while ArcLogProd.tell() < tamArch:
					regProd = pickle.load(ArcLogProd)
					print(str(regProd.codigo) + '\t' + regProd.nombre)
				cod = int(input('\n¿Cual desea eliminar? Ingrese el codigo: '))
				while cod <= 0 or cod >= 100000:
					print('Codigo incorrecto!')
					cod = int(input('¿Cual desea eliminar? Ingrese el codigo: '))

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
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				while ArcLogProd.tell() < tamArch:
					regProd = pickle.load(ArcLogProd)
					print(str(regProd.codigo) + '\t' + regProd.nombre)

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
				ArcLogProd.seek(0,0)
				tamArch = os.path.getsize(ArcFisiProd)
				while ArcLogProd.tell() < tamArch:
					regProd = pickle.load(ArcLogProd)
					print(str(regProd.codigo) + '\t' + regProd.nombre)

				cod = int(input('\n¿Cual desea eliminar? Ingrese el codigo: '))
				while cod <= 0 or cod >= 100000:
					print('Codigo incorrecto!')
					cod = int(input('¿Cual desea eliminar? Ingrese el codigo: '))

				ban = False
				ArcLogProd.seek(0,0)
				while ArcLogProd.tell() < tamArch and ban == False:
					puntero = ArcLogProd.tell()
					regProd = pickle.load(ArcLogProd)
					if int(regProd.codigo) == cod:
						ArcLogProd.seek(puntero,0)
						ban = True
						regProd.codigo = int(input('Ingrese el codigo nuevo: '))
						while regProd.codigo <= 0 or regProd.codigo >= 100000:
							print('Codigo incorrecto!')
							regProd.codigo = int(input('Ingrese el codigo nuevo:'))
						regProd.nombre = str(input('\nIngrese el nombre nuevo: ').upper())
						while len(regProd.nombre) <= 0 or len(regProd.nombre) > 15:
							print('Largo del nombre incorrecto!')
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
				print('Opcion invalida!')
				os.system('pause')
		elif type == "Rubros":
			if menu_option == 'A':
				regRubro.codigo = int(input('Ingrese el codigo: '))
				while regRubro.codigo <= 0 or regRubro.codigo >= 100000:
					print('Codigo incorrecto!')
					regRubro.codigo = int(input('Ingrese el codigo:'))
				regRubro.nombre = str(input('\nIngrese el nombre: ').upper())
				while len(regRubro.nombre) <= 0 or len(regRubro.nombre) > 15:
					print('Largo del nombre incorrecto!')
					regRubro.nombre = str(input('Ingrese el nombre: ').upper())
				formatearProductos(regRubro)
				ArcLogRubro.seek(0,2)
				pickle.dump(regRubro, ArcLogRubro)
				ArcLogRubro.flush()
				ordenaRubro()

			elif menu_option == 'B':
				print('Esta funcionalidad esta en construccion')
				os.system('pause')
			elif menu_option == 'C':
				print('Listado de rubro(s):')
				print('\nCodigo\tNombre')
				ArcLogRubro.seek(0,0)
				tamArch = os.path.getsize(ArcFisiRubro)
				while ArcLogRubro.tell() < tamArch:
					regRubro = pickle.load(ArcLogRubro)
					print(str(regRubro.codigo) + '\t' + regRubro.nombre)

				os.system('pause')
			elif menu_option == 'M':
				print('Esta funcionalidad esta en construccion')
				os.system('pause')	
			elif menu_option == 'V':
				print('')
			else:
				print('Opcion invalida!')
				os.system('pause')
		elif type == "Rubros X Producto":
			if menu_option == 'A':
				regRuXPro.codigo_rubro = int(input('Ingrese el codigo del rubro: '))
				while regRuXPro.codigo_rubro <= 0 or regRuXPro.codigo_rubro >= 100000:
					print('Codigo incorrecto!')
					regRuXPro.codigo_rubro = int(input('Ingrese el codigo del rubro: '))
	
				regRuXPro.codigo_producto = int(input('\nIngrese el codigo del producto: '))
				while regRuXPro.codigo_producto <= 0 or regRuXPro.codigo_producto >= 100000:
					print('Codigo incorrecto!')
					regRuXPro.codigo_producto = int(input('Ingrese el codigo del producto: '))

				regRuXPro.valor_minimo_admitido = int(input('\nIngrese el valor minimo admitido: '))
				while regRuXPro.valor_minimo_admitido < 0:
					print('Minimo menor que 0!')
					regRuXPro.valor_minimo_admitido = int(input('Ingrese el valor minimo admitido: '))
				
				regRuXPro.valor_maximo_admitido = int(input('\nIngrese el valor maximo admitido: '))
				while regRuXPro.valor_maximo_admitido > 100 and regRuXPro.valor_maximo_admitido > regRuXPro.valor_minimo_admitido:
					print('Maximo mayor que 100 o menor/igual que el valor minimo!')
					regRuXPro.valor_maximo_admitido = int(input('Ingrese el valor valor maximo admitido: '))

				formatearProductos(regRuXPro)
				ArcLogRuXPro.seek(0,2)
				pickle.dump(regRuXPro, ArcLogRuXPro)
				ArcLogRuXPro.flush()

			elif menu_option == 'B':
				print('Esta funcionalidad esta en construccion')
				os.system('pause')
			elif menu_option == 'C':
				print('Esta funcionalidad esta en construccion')
				os.system('pause')
			elif menu_option == 'M':
				print('Esta funcionalidad esta en construccion')
				os.system('pause')	
			elif menu_option == 'V':
				print('')
			else:
				print('Opcion invalida!')
				os.system('pause')
			os.system('pause')
		elif type == "Silos":
			if menu_option == 'A':
				regSilos.codigo_silo = int(input('Ingrese el codigo del silo: '))
				while regSilos.codigo_silo <= 0 or regSilos.codigo_silo >= 100000:
					print('Codigo incorrecto!')
					regSilos.codigo_silo = int(input('Ingrese el codigo del silo:'))

				regSilos.nombre = str(input('\nIngrese el nombre del silo: ').upper())
				while len(regSilos.nombre) <= 0 or len(regSilos.nombre) > 15:
					print('Largo del nombre incorrecto!')
					regSilos.nombre = str(input('Ingrese el nombre del silo: ').upper())

				regSilos.codigo_producto = int(input('\nIngrese el codigo del producto: '))
				while regSilos.codigo_producto <= 0 or regSilos.codigo_producto >= 100000:
					print('Codigo incorrecto!')
					regSilos.codigo_producto = int(input('Ingrese el codigo del producto:'))

				formatearProductos(regRubro)
				ArcLogRubro.seek(0,2)
				pickle.dump(regRubro, ArcLogRubro)
				ArcLogRubro.flush()

			elif menu_option == 'B':
				print('Esta funcionalidad esta en construccion')
				os.system('pause')
			elif menu_option == 'C':
				print('Esta funcionalidad esta en construccion')
				os.system('pause')
			elif menu_option == 'M':
				print('Esta funcionalidad esta en construccion')
				os.system('pause')	
			elif menu_option == 'V':
				print('')
			else:
				print('Opcion invalida!')
				os.system('pause')
			os.system('pause')
		elif type == "Sucursales":
			print('Esta funcionalidad esta en construccion')
			os.system('pause')
		elif type == "Rubros X Titular":
			print('Esta funcionalidad esta en construccion')
			os.system('pause')


# Enteros: ban, i, s, h, opcion
# Cadenas: opcion2
def entrega_de_cupos():
	global total_cupos
	global cant_productos

	global patentes
	global cupones 
	global estado
	#global producto
	global productos

	opcion2 = ''
	ban = 0
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
	global total_camiones

	global patentes
	global estado
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

# Cadenas: buscar
# Enteros: ban, i
def registrar_peso_bruto():
	global patentes
	global estado
	global pesos_brutos

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
	global patentes
	global estado
	global pesos_brutos
	global taras

	global pesos_netos_productos
	#global productos
	global producto

	global mayor_menor_productos
	global patente_mm_productos
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
def ordenar_mostrar(producto: list[str],patentes: list[str], pesos_brutos: list[int], taras: list[int]):
	"""
	for i in range(7):
		for h in range(i+1,8):
			if (pesos_brutos[h]-taras[h]) > (pesos_brutos[i]-taras[i]):
				aux = pesos_brutos[i]
				pesos_brutos[i] = pesos_brutos[h]
				pesos_brutos[h] = aux

				aux = taras[i]
				taras[i] = taras[h]
				taras[h] = aux

				aux = patentes[i]
				patentes[i] = patentes[h]
				patentes[h] = aux

				aux = producto[i]
				producto[i] = producto[h]
				producto[h] = aux

	print('\nListado de camione(s) ordenados descendentemente por peso neto:')
	i = 0
	if patentes[i] != '':
		while i < 8:
			print(f'- {patentes[i]} | {producto[i]} | {(pesos_brutos[i]-taras[i]):.2f}')
			if patentes[i] == '':
				i = 7
			i = i + 1
	else:
		print('No hay ningun camion listado!')
	"""
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
	
	global total_cupos
	global total_camiones 

	total_cupos = 0
	total_camiones = 0

	global mayor_menor_productos
	mayor_menor_productos = [[0,0],[0,0],[0,0]]

	global patente_mm_productos
	patente_mm_productos = [['',''],['',''],['','']]

	global pesos_netos_productos
	pesos_netos_productos = [0] * 3

	global cant_productos
	cant_productos = [0] * 3

	#global productos
	#productos = [''] * 3

	global producto 
	producto = [''] * 8

	global patentes
	patentes = [''] * 8

	global pesos_brutos
	pesos_brutos = [0] * 8

	global taras
	taras = [0] * 8

	global cupones
	cupones = [0] * 8

	global estado
	estado = [''] * 8

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
		print('[0] Salir')
		menu_option: str = input('Opcion: ')

		if menu_option == '1':
			administraciones()
		elif menu_option == '2':
			os.system('cls')
			entrega_de_cupos()
			os.system('pause')
		elif menu_option == '3':
			os.system('cls')
			recepcion()
			os.system('pause')
		elif menu_option == '4':
			os.system('cls')
			print('Esta funcionalidad esta en construccion')
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
			reportes()
			os.system('pause')
		elif menu_option == '0':
			ArcLogOpera.close()
			ArcLogProd.close()
			ArcLogRubro.close()
			ArcLogSilos.close()
			ArcLogRuXPro.close()
			print('')
		else:
			print('Opcion invalida!')
			os.system('pause')


if __name__ == '__main__':
	menu_principal() #Este pedazo de código sirve para que un programa externo no pueda ejecutar este código