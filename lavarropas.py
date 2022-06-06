from aparato import Aparato
class Lavarropas(Aparato):
    __capacidadLavado=''
    __velocidadCentrifugado=''
    __cantiProgramas=0
    __tipoCarga=''
    def __init__(self,marca,modelo,color,pais,precio,capacidadLavado,velocidadCentrifugado,cantiProgramas,tipoCarga):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidadLavado=capacidadLavado
        self.__velocidadCentrifugado=velocidadCentrifugado
        self.__cantiProgramas=cantiProgramas
        self.__tipoCarga=tipoCarga
    def getPais(self):
        return super().getPais()
    def getMarca(self):
        return super().getMarca()
    def getPrecioBase(self):
        return super().getPrecioBase()
    def getCapacidadLavado(self):
        return self.__capacidadLavado
    def getTipo(self):
        return 'Lavarropa'
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                capacidadLavado=self.__capacidadLavado,
                velocidadCentrifugado=self.__velocidadCentrifugado,
                cantiProgramas=self.__cantiProgramas,
                tipóCarga=self.__tipoCarga
                )
                )
        return d
