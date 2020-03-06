from lxml import etree
doc = etree.parse('ARMADORES.xml')

# Listar información: Lista los nombres, apellido, ciudad, dni y el
#                     teléfono de los armadores.

def listar_informacion():
	listaArmadores=[]
	lista_nombre = doc.xpath("/ARMADORES/armador/nombre/text()")
	for nombre in lista_nombre:
		dicArmadores={}
		apellidos = doc.xpath('/ARMADORES/armador[nombre="%s"]//apellidos/text()'%nombre)
		ciudad = doc.xpath('/ARMADORES/armador[nombre="%s"]//ciudad/text()'%nombre)
		dni =  doc.xpath('/ARMADORES/armador[nombre="%s"]//dni/text()'%nombre)
		telefono = doc.xpath('/ARMADORES/armador[nombre="%s"]//telefono/text()'%nombre)

		dicArmadores={"nombre":nombre, "apellidos":apellidos[0], "ciudad":ciudad[0], "dni":dni[0], "telefono":telefono[0] }
		listaArmadores.append(dicArmadores)
	return listaArmadores


# Contar información: Lista los dni de los armadores y el total
#                     de barcos que tiene.

def contar_informacion():
	dicTotalBarco={}
	dni_lista = doc.xpath("/ARMADORES/armador/dni/text()")
	for dni in dni_lista:
		total_barco = doc.xpath('count(/ARMADORES/armador[dni="%s"]//barcos/barco)'%dni)
		dicTotalBarco[dni] = total_barco
	return dicTotalBarco


# Buscar o filtrar información: Mostrar las armadores que pertenecen
#                               a un determinado país.

def buscar_filtrar_informacion(pais):
	lista_nombre = doc.xpath('/ARMADORES/armador/ciudad[contains(text(), "%s")]/../nombre/text()'%pais)
	return lista_nombre

# Buscar información relacionada: Pide por teclado una matricula y
#                                 muestra el nombre del armador y el dni.

def buscar_informacion_relacionada(matricula):
	nombre = doc.xpath('/ARMADORES/armador/barcos/barco[@matricula="%s"]/../../nombre/text()'%matricula)
	dni = doc.xpath('/ARMADORES/armador/barcos/barco[@matricula="%s"]/../../dni/text()'%matricula)
	lista = [nombre[0], dni[0]]
	return lista


# Ejercicio libre: Pide un mínimo y un máximo de eslora y te salen los
#                  nombre de los barcos con el nombre del armador y el teléfono.


def ejercicio_libre(min, max):
	lista_barco=[]
	lista_nombre_barco = doc.xpath('/ARMADORES/armador/barcos/barco[eslora > %i and eslora < %i]/nombre/text()'%(min, max))
	for nombre_barco in lista_nombre_barco:
		nombre_armador = doc.xpath('/ARMADORES/armador/barcos/barco[nombre="%s"]/../../nombre/text()'%nombre_barco)
		telefono_armador = doc.xpath('/ARMADORES/armador/barcos/barco[nombre="%s"]/../../telefono/text()'%nombre_barco)
		lista=[nombre_barco, nombre_armador[0], telefono_armador[0]]
		lista_barco.append(lista)
	return lista_barco



