from aparato import Aparato
class Heladera(Aparato):
    __capacidadLitros=0
    __freezer=False
    __ciclica=False
    def __init__(self,marca,modelo,color,pais,precio,capacidadLitros,freezer,ciclica):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidadLitros=capacidadLitros
        self.__freezer=freezer
        self.__ciclica=ciclica
    def getPais(self):
        return super().getPais()
    def getTipo(self):
        return 'Heladera'
    def getMarca(self):
        return super().getMarca()
    def getFreezer(self):
        return self.__freezer
    def getCiclica(self):
        return self.__ciclica
    def getPrecioBase(self):
        return super().getPrecioBase()
    def __str__(self):
        print('Capacidad:{} Freezer:{} Cilcica:{}'.format(self.__capacidadLitros,self.__freezer,self.__ciclica))
        return super().__str__()
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                capacidadLitros=self.__capacidadLitros,
                freezer=self.__freezer,
                ciclica=self.__ciclica
                )
                )
        return d
