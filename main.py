from coleccion import Manejador
from objectencoder import ObjectEncoder
from menu import Menu
if __name__=='__main__':
    menu=Menu()
    jsonF=ObjectEncoder()
    aparatos = Manejador()
    diccionario=jsonF.leerJSONArchivo('aparatoselectronicos.json')
    aparatos=jsonF.decodificarDiccionario(diccionario)
    print('archivo leido!')
    salir=False
    while not salir:
        print('------------------------------------------')
        print('1.Insertar un aparato')
        print('2.Agregar aparato')
        print('3.Dada una Posicion Mostrar')
        print('4.Aparatos Marca Phillips')
        print('5.Mostrar Marca de lavarropas con carga superior')
        print('6.Mostrar aparatos')
        print('7.Almacenar los objetos en el archivo JSON')
        print('8.salir')
        print('------------------------------------------')
        op=input('->')
        menu.opcion(op,aparatos,jsonF)
        salir = op =='8'
