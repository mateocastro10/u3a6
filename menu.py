from coleccion import Manejador as MJ
from objectencoder import ObjectEncoder as Encoder
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         '5':self.opcion5,
                         '6':self.opcion6,
                         '7':self.opcion7,
                         '8':self.salir}
    def opcion(self,op,Manejador,JSONF):
        func=self.__switcher.get(op,lambda:'opcion incorrecta!')
        if(op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6' or op=='7'):
            func(Manejador,JSONF)
        else:
            func()
    def opcion1(self,Manejador,JSONF):
        if(type(Manejador)==MJ):
            print('-----------Insertar heladera-----------')
            Manejador.punto1()
    def opcion2(self,Manejador,JSONF):
        if(type(Manejador)==MJ):
            Manejador.punto2()
    def opcion3(self,Manejador,JSONF):
        if(type(Manejador)==MJ):
            Manejador.punto3()
    def opcion4(self,Manejador,JSONF):
        if(type(Manejador)==MJ,JSONF):
            Manejador.punto4()
    def opcion5(self,Manejador,JSONF):
        if(type(Manejador)==MJ,JSONF):
            Manejador.punto5()
    def opcion6(self,Manejador,JSONF):
        if(type(Manejador)==MJ,JSONF):
            Manejador.punto6()
    def opcion7(self,Manejador,JSONF):
        if(type(Manejador)==MJ and type(JSONF)==Encoder):
            d=Manejador.toJSON()
            JSONF.guardarJSONArchivo(d,'aparatoselectronicos.json')
            print('SUBIDO CON EXITO')
    def salir(self):
        print('finalizando')
