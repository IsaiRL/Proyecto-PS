import subprocess #El módulo le permite generar nuevos procesos, conectarse a sus tuberías de entrada / salida / error y obtener sus códigos de retorno
import sys      #importando modulo  que provee acceso a funciones y objetos mantenidos por del interprete.
import unicodedata #importando modulo para cadena de caractres
import logging  #importando modulo para logs

#aqui se determina donde se gardara el log 
logging.basicConfig(filename='/home/uzielcv/Documentos/prograSegura/Proyecto-Final/monitoreo.log',filemode='a', format='%(asctime)s - (name)s - %(levelname)s - %(message)s')



#se creo esta exepcion para que se lanze cada vez que se introdusca otra cosa que no sean los monitoreos
class MyClassepalabraInvalidaException(Exception):
    pass

#ayuda para ver como se usa
def ayuda():
	print('ayuda para programa basico para monitoreo')
	print('solo se cuentan con las opcciones de cpu , memoria y disco ')
	print('disponible solo para linux')
	print('para usarse solo se escribie el que se quiere ver')
	print('ejemplo:')
	print('python monitor.py disco')
	print('python monitor.py cpu')
	print('python monitor.py memoria')

def compara_palabra(text):
# aqui se compran las palabras para que aun usando mayusculas funcione el monitoreo
	string1=str('cpu')
	string2=str('memoria')
	string3=str('disco')
	string4=str('ayuda')

	if text.lower() == string1.lower():
		return string1
	if text.lower() == string2.lower():
		return string2
	if text.lower() == string3.lower():
		return string3
	if text.lower() == string4.lower():
		return string4

def uso_cpu():

	#comando para obtener el porcentaje de cpu
	cpu=subprocess.getoutput("top -b -n1 | grep 'Cpu(s)'")
	# devolvemos el % de uso
	print (cpu)

def uso_memorias():

	#comando para obtener porcentaje de memorias
	memorias=subprocess.getoutput("top -b -n1 | grep 'KiB Mem'")
	# devolvemos el uso de memorias
	print (memorias)

def uso_disco():

	#comando para obtener porcentaje de discos
	disco=subprocess.getoutput("df -h -t ext4 --output=source,size,pcent")
	#devolvemos el uso de disco
	print (disco)

if __name__ == '__main__':


	try:
		accionM = sys.argv[1]
	except IndexError as error:
		logging.error('se ingreso elemento incorrecto o no se ingreo elemento',exc_info=True)


	try:
		palabra=compara_palabra(accionM)
		if palabra == 'cpu':
			uso_cpu()
		else:
			if palabra == 'memoria':
				uso_memorias()
			else:
				if palabra == 'disco':
					uso_disco()
				else:
					if palabra == 'ayuda':
						ayuda()
					else :
						raise MyClassepalabraInvalidaException('palabra no valida')

	except MyClassepalabraInvalidaException as error:
		logging.error('no son acciones validas',exc_info=True)
	except Exception as error:
		logging.error('algo salio mal',exc_info=True)
	finally:
		print('bye')




