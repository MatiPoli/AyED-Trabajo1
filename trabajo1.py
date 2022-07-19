#Integrantes:
#-Matías Marquez (107)
#-Alex Diaz (107)
#-Marcos Godoy (108)
#-Valentin Dalmau (108)

import os

def administraciones() -> None:
	admin_option = ''
	while admin_option != 'V':
		os.system('cls')
		print('MENU ADMINISTRACIONES')
		print('[A] Titulares')
		print('[B] Productos')
		print('[C] Rubros')
		print('[D] Rubros X Producto')
		print('[E] Silios')
		print('[F] Sucursales')
		print('[G] Rubros X Titular')
		print('[V] Volver al menu principal')
		admin_option: str = input('Opcion: ').upper()

		if admin_option == 'A':
			menu('titulares')
		elif admin_option == 'B':
			menu('productos')
		elif admin_option == 'C':
			menu('rubros')
		elif admin_option == 'D':
			menu('rubros x producto')
		elif admin_option == 'E':
			menu('silios')
		elif admin_option == 'F':
			menu('sucursales')
		elif admin_option == 'G':
			menu('rubros x titular')
		elif admin_option == 'V':
			print('')
		else:
			print('Opcion invalida!')
			os.system('pause')



def menu(type: str) -> None:
	global productos
	global cant_productos
	menu_option = ''
	while menu_option != 'V':
		os.system('cls')
		print(f'MENU {type.upper()}')
		print('[A] Alta')
		print('[B] Baja')
		print('[C] Consulta')
		print('[M] Modificacion')
		print('[V] Volver al menu anterior')
		menu_option: str = input('Opcion: ').upper()
		if type == "productos":
			if menu_option == 'A':
				ban = 0
				for i in range(3):
					if productos[i] == '' and ban != 1:
						ban = 1
						productos[i] = str(input('Ingrese el nombre del producto: ').upper())
				if ban == 0:
					print('Se ha llenado la lista de productos, pruebe a modificarla.')
				os.system('pause')
			elif menu_option == 'B':
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
			elif menu_option == 'C':
				print('Listado de producto(s):')
				for i in range(3):
					print("- " + productos[i])
				os.system('pause')
			elif menu_option == 'M':
				print('Listado de producto(s):')
				for i in range(3):
					print(str(i) + ") " + productos[i])
				opcion = int(input('¿Cual desea modificar? Ingrese el numero: '))
				if opcion >= 0 and opcion <= 2 and productos[opcion] != '':
					productos[opcion] = str(input('Ingrese el nuevo nombre: ').upper())
				else:
					print("Opcion invalida u opcion vacia!")
				os.system('pause')
			elif menu_option == 'V':
				print('')
			else:
				print('Opcion invalida!')
				os.system('pause')
		else:
			if menu_option == 'A':
				print('Esta funcionalidad esta en construccion')
				os.system('pause')
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



def entrega_de_cupos():
	global total_cupos
	global cant_productos

	global patentes
	global cupones 
	global estado
	global producto

	global productos
	opcion2 = ''
	ban = 0
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



def recepcion():
	global total_camiones

	global patentes
	global estado

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



def registrar_peso_bruto():
	global patentes
	global estado
	global pesos_brutos


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



def registrar_tara():
	global patentes
	global estado
	global pesos_brutos
	global taras

	global pesos_netos_productos
	global productos
	global producto

	global mayor_menor_productos
	global patente_mm_productos

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

def ordenar_mostrar(producto: list[str],patentes: list[str], pesos_brutos: list[int], taras: list[int]):

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



def menu_principal() -> None:
	
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

	global productos
	productos = [''] * 3

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
			print('')
		else:
			print('Opcion invalida!')
			os.system('pause')


if __name__ == '__main__':
	menu_principal() #Este pedazo de código sirve para que un programa externo no pueda ejecutar este código