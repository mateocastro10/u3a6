class Aparato:
    __marca = ''
    __modelo = ''
    __color = ''
    __paisdefabricacion = ''
    __preciobase = 0.0

    def __init__(self, marca, modelo, color, pais, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisdefabricacion = pais
        self.__preciobase = precio

    def getPais(self):
        self.__paisdefabricacion

    def getPrecioBase(self):
        return self.__preciobase

    def getMarca(self):
        return self.__marca

    def __str__(self):
        return ('Marca:{} Modelo:{} Color:{} Pais de Fabricacion:{} Precio Base:{}'.format(self.__marca, self.__modelo,
                                                                                           self.__color,
                                                                                           self.__paisdefabricacion,
                                                                                           self.__preciobase))
