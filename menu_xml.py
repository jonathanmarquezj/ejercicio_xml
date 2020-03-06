#!/usr/bin/python
from funciones import *

def mostrar_menu():
	print("1 - Listar información")
	print("2 - Contar información")
	print("3 - Buscar o filtrar información")
	print("4 - Buscar información relacionada")
	print("5 - Ejercicio libre")
	print("0 - Salir")

mostrar_menu()

menu = int(input("-> "))

while menu != 0:
	if menu == 1:
		# 1 - Listar información
		print("-------------------------------")
		for lista in listar_informacion():
			print("Nombre: \t", lista['nombre'])
			print("Apellidos: \t", lista['apellidos'])
			print("Ciudad: \t", lista['ciudad'])
			print("DNI: \t\t", lista['dni'])
			print("Telefono: \t", lista['telefono'])
			print("-------------------------------")
	elif menu == 2:
		# 2 - Contar información
		print("-------------------------------")
		for i,j in contar_informacion().items():
			print("DNI: ", i, "\t Total barcos:", j)
	elif menu == 3:
		# 3 - Buscar o filtrar información
		print("-------------------------------")
		pais = str(input("Pais: "))
		for nombre in buscar_filtrar_informacion(pais):
			print("Nombre: ", nombre)
	elif menu == 4:
		# 4 - Buscar información relacionada
		print("-------------------------------")
		print("DUEÑO DEL BARCO")
		matricula = str(input("Matricula: "))
		datos_armador = buscar_informacion_relacionada(matricula)
		for dato in datos_armador:
			print(dato)
	elif menu == 5:
		# 5 - Ejercicio libre
		print("-------------------------------")
		min = int(input("Tamaño de eslora minimo: "))
		max = int(input("Tamaño de eslora maximo: "))
		lista_barco = ejercicio_libre(min, max)
		for lista in lista_barco:
			print("-------------------------------")
			for barco in lista:
				print(barco)
	else:
		print("-------------------------------")
		print("ORDEN NO ENCONTRADA")
		print("-------------------------------")



	mostrar_menu()
	menu = int(input("-> "))

print("-------------------------------")
print("Adios :)")
print("-------------------------------")

