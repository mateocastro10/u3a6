from pkgutil import ImpLoader
from zope.interface import implementer
from heladera import Heladera
from lavarropas import Lavarropas
from televisor import Televisor
# from ej5 import Iinterface
from nodo import Nodo


# @implementer(Iinterface)
class Manejador:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def insertarElemento(self, posicion, elemento):
        aux = self.__comienzo
        band = True
        j = 0
        nodo = Nodo(elemento)
        if (posicion == 0):
            nodo.setSiguiente(aux)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
            print('Insertado al comienzo')
        else:
            while (band):
                if (j == posicion):
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    band = False
                aux = aux.getSiguiente()
                j += 1

    def agregarElemento(self, elemento):
        # para agregar un elemento al final de una colección
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def mostrarElemento(self):
        id = int(input('Ingrese posicion de el elemento que desea encontrar:'))
        aux = self.__comienzo
        i = 1
        while aux != None:
            if (i == id):
                print(aux.getDato())
                aux = None
            else:
                i += 1
                aux = aux.getSiguiente()

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[aparato.toJSON() for aparato in self]
        )
        return d

    def punto1(self):
        marca = input('ingrese marca:')
        modelo = input('ingrese modelo:')
        color = input('ingrese color:')
        pais = input('ingrese pais:')
        precio = float(input('ingrese precio:'))
        capacidad = input('ingrese capacidad de litros:')
        print('Tiene freezer?(1.si|2.no)')
        op1 = input('->')
        if (op1 == '1'):
            freezer = True
        else:
            freezer = False
        print('Es ciclica?(1.si|2.no)')
        op2 = input('->')
        if (op2 == '1'):
            ciclica = True
        else:
            ciclica = False
        pos = int(input('Ingrese posicion:'))
        unaheladera = Heladera(marca, modelo, color, pais, precio, capacidad, freezer, ciclica)
        self.insertarElemento(pos, unaheladera)

    def punto2(self):
        op = input('Que aparato desea agregar(1.heladera|2.lavarropa|3.televisor)')
        marca = input('ingrese marca:')
        modelo = input('ingrese modelo:')
        color = input('ingrese color:')
        pais = input('ingrese pais de origen:')
        precio = float(input('ingrese precio:'))
        if (op == '1'):
            capacidad = input('ingrese capacidad de litros:')
            print('Tiene freezer?(1.si|2.no)')
            op1 = input('->')
            if (op1 == '1'):
                freezer = True
            else:
                freezer = False
            print('Es ciclica?(1.si|2.no)')
            op2 = input('->')
            if (op2 == '1'):
                ciclica = True
            else:
                ciclica = False
            aparato = Heladera(marca, modelo, color, pais, precio, capacidad, freezer, ciclica)
        elif (op == '2'):
            capacidadLavado = int(input('ingrese capacidad de Lavado:'))
            velocidadCentrifugado = input('ingrese velocidad de centrifugado:')
            cantiProgramas = input('ingrese cantidad de programas:')
            tipoCarga = input('ingrese el tipo de carga( Frontal, Superior):')
            aparato = Lavarropas(marca, modelo, color, pais, precio, capacidadLavado, velocidadCentrifugado,
                                 cantiProgramas, tipoCarga)
        elif (op == '3'):
            tipoPantalla = input(
                'ingrese tipo de pantalla (crt, vga, svga, plasma, lcd, led, TouchScreen, MultiTouch):')
            pulgadas = input('ingrese pulgadas de la tv:')
            tipoDefinicion = input('ingrese la definicion(HD,SD,FULL HD):')
            op1 = input('tiene conexion?(1.si|2.no)')
            if (op1 == '1'):
                conexion = True
            else:
                conexion = False
            aparato = Televisor(marca, modelo, color, pais, precio, tipoPantalla, pulgadas, tipoDefinicion, conexion)
        self.agregarElemento(aparato)
        print('Aparato Agregado')

    def punto3(self):
        self.mostrarElemento()

    def punto4(self):
        j = 0
        for i in self:
            if (i.getMarca().lower() == 'Phillips'):
                j += 1
        print('la cantidad de aparatos de la marca Phillips son:{} '.format(j))

    def punto5(self):
        for i in self:
            if (i.getTipo().lower() == 'lavarropa'):
                if (i.getCarga().lower() == 'superior'):
                    print('Marca del lavarropas:{} '.format(i.getMarca()))

    def importeTelevision(self, elemento):
        total = elemento.getPrecioBase()
        definicion = elemento.getTipoDefinicion().lower()
        internet = elemento.getConexion()
        if definicion == 'sd':
            imp1 = total + (total / 100)
        elif definicion == 'hd':
            imp1 = total + (total * 2 / 100)
        elif definicion == 'full hd':
            imp1 = total + (total * 3 / 100)
        if internet == True:
            imp1 += total + (total * 10 / 100)
        return imp1

    def importeLavarropas(self, elemento):
        total = elemento.getPrecioBase()
        capacidad = elemento.getCapacidadLavado()
        if capacidad <= 5:
            imp3 = total + (total / 100)
        elif capacidad > 5:
            imp3 = total + (total * 3 / 100)
        return imp3

    def importeHeladera(self, elemento):
        total = elemento.getPrecioBase()
        freezer = elemento.getFreezer()
        ciclica = elemento.getCiclica()
        if freezer:
            imp2 = total + (total * 5 / 100)
        else:
            imp2 = total + (total / 100)
        if ciclica:
            imp2 += total + (total * 10 / 100)
        return imp2

    def punto6(self):
        for i in self:
            print('Marca:{} Pais:{}'.format(i.getMarca(), i.getPais()))
            if i.getTipo().lower() == 'televisor':
                imp = self.importeTelevision(i)
                print('importe de venta:{}'.format(imp))
            elif i.getTipo().lower() == 'heladera':
                imp = self.importeHeladera(i)
                print('importe de venta:{}'.format(imp))
            elif i.getTipo().lower() == 'lavarropa':
                imp = self.importeLavarropas(i)
                print('importe de venta:{}'.format(imp))
