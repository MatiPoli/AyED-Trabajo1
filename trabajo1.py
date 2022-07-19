import os

def menu(type: str) -> None:
	menu_run: bool = True
	while menu_run:
		os.system('cls')
		print(f'MENU {type.upper()}')
		print('[A] Alta')
		print('[B] Baja')
		print('[C] consulta')
		print('[M] Modificacion')
		print('[V] Volver al menu anterior')
		menu_option: str = input('Opcion: ').upper()

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
			menu_run = False
		else:
			print('Opcion invalida!')
			os.system('pause')

def recepcion():
	global total_camiones
	global total_camiones_soja
	global total_camiones_maiz
	global neto_total_soja
	global neto_total_maiz
	global patente_mayor_soja
	global peso_mayor_soja
	global patente_menor_maiz
	global peso_menor_maiz
	recepcion_run: bool = True
	while recepcion_run:
		os.system('cls')
		patente: str = input('Ingresa la patente: ').upper()
		run: bool = True
		while run:
			producto: str = input('Elija el producto (S-soja, M-maiz): ').upper()
			if producto in ['SOJA', 'MAÍZ', 'S', 'M', 'MAIZ']:
				run = False
			else:
				print('Producto no registrado o incorrecto')
		peso_bruto: int = int(input('Ingrese el peso en kg: '))
		while peso_bruto < 0:
			print('Valor incorrecto')
			peso_bruto: int = int(input('Ingrese el peso en kg: '))
		tara: int = int(input('Ingrese la tara en kg: '))
		while tara < 0 or tara > peso_bruto:
			print('Valor incorrecto')
			tara: int = int(input('Ingrese la tara en kg: '))
		peso_neto = peso_bruto - tara
		if producto in ['SOJA','S']:
			total_camiones_soja += 1
			neto_total_soja += peso_neto
			if peso_mayor_soja == 0:
				patente_mayor_soja = patente
				peso_mayor_soja = peso_neto
			elif peso_mayor_soja < peso_neto:
				patente_mayor_soja = patente
				peso_mayor_soja = peso_neto
		if producto in ['MAIZ','M','MAÍZ']:
			total_camiones_maiz += 1
			neto_total_maiz += peso_neto
			if peso_menor_maiz == 0:
				patente_menor_maiz = patente
				peso_menor_maiz = peso_neto
			elif peso_menor_maiz > peso_neto:
				patente_menor_maiz = patente
				peso_menor_maiz = peso_neto
		print(f'\nEl peso neto del camion es: {peso_neto}')
		total_camiones += 1
		opcion: str = input('Desea ingresar otro camion? (S/N): ').upper()
		while opcion not in ['YES', 'NO', 'N' , 'SI' , 'Y' , 'S']:
			print('Opcion incorrecta')
			opcion: str = input('Desea ingresar otro camion? (S/N): ').upper()
		if opcion in ['NO' , 'N']:
			recepcion_run = False

def reportes():
	global total_camiones
	global total_camiones_soja
	global total_camiones_maiz
	global neto_total_soja
	global neto_total_maiz
	global patente_mayor_soja
	global peso_mayor_soja
	global patente_menor_maiz
	global peso_menor_maiz
	os.system('cls')
	print('REPORTES')
	print(f'Cantidad total de camiones que llegaron: {total_camiones}')
	print(f'Cantidad total de camiones de soja: {total_camiones_soja}')
	print(f'Cantidad total de camiones de maiz: {total_camiones_maiz}')
	print(f'Peso neto total de soja: {neto_total_soja}')
	print(f'Peso neto total de maiz: {neto_total_maiz}')
	promedio: float
	if total_camiones_soja == 0:
		promedio = 0
	else:
		promedio = neto_total_soja / total_camiones_soja
	print(f'Promedio del peso neto de soja: {promedio:.2f}')
	if total_camiones_maiz == 0:
		promedio = 0
	else:
		promedio = neto_total_maiz / total_camiones_maiz
	print(f'Promedio del peso neto de maiz: {promedio:.2f}')
	print(f'Patente del camion con mayor peso neto de soja: {patente_mayor_soja}')
	print(f'Patente del camion con meso peso neto de maiz: {patente_menor_maiz}')
def administraciones() -> None:

	admin_run: bool = True
	while admin_run:
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
			admin_run = False
		else:
			print('Opcion invalida!')
			os.system('pause')

def menu_principal() -> None:
	
	global total_camiones
	global total_camiones_soja
	global total_camiones_maiz
	global neto_total_soja
	global neto_total_maiz
	global patente_mayor_soja
	global peso_mayor_soja
	global patente_menor_maiz
	global peso_menor_maiz

	total_camiones = 0
	total_camiones_soja = 0
	total_camiones_maiz = 0
	neto_total_soja = 0
	neto_total_maiz = 0
	patente_mayor_soja = '-'
	peso_mayor_soja = 0
	patente_menor_maiz = '-'
	peso_menor_maiz = 0

	menu_run: bool = True
	while menu_run:
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
			print('Esta funcionalidad esta en construccion')
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
			print('Esta funcionalidad esta en construccion')
			os.system('pause')
		elif menu_option == '6':
			os.system('cls')
			print('Esta funcionalidad esta en construccion')
			os.system('pause')
		elif menu_option == '7':
			os.system('cls')
			print('Esta funcionalidad esta en construccion')
			os.system('pause')
		elif menu_option == '8':
			reportes()
			os.system('pause')
		elif menu_option == '0':
			menu_run = False
		else:
			print('Opcion invalida!')
			os.system('pause')


if __name__ == '__main__':
	menu_principal() #Este pedazo de código sirve para que un programa externo no pueda ejecutar este código