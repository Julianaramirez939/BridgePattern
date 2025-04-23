# Abstracción: La clase Dispositivo
class Dispositivo:
    def __init__(self, implementacion):
        self.implementacion = implementacion

    def encender(self):
        self.implementacion.encender()

    def apagar(self):
        self.implementacion.apagar()

    def establecer_canal(self, canal):
        self.implementacion.establecer_canal(canal)


# Implementaciones Concretas
class TVImplementacion:
    def encender(self):
        print("TV: Encendiendo")

    def apagar(self):
        print("TV: Apagando")

    def establecer_canal(self, canal):
        print(f"TV: Estableciendo canal en {canal}")


class RadioImplementacion:
    def encender(self):
        print("Radio: Encendiendo")

    def apagar(self):
        print("Radio: Apagando")

    def establecer_canal(self, canal):
        print(f"Radio: Sintonizando estación {canal}")

# DVD implementacion 
class DVDImplementacion:
    def encender(self):
        print("DVD: Encendiendo")

    def apagar(self):
        print("DVD: Apagando")

    def establecer_canal(self, canal):
        print(f"DVD: Sintonizando canal de audio {canal}")



# Clientes
tv = Dispositivo(TVImplementacion())
radio = Dispositivo(RadioImplementacion())
dvd = Dispositivo(DVDImplementacion())

tv.encender()
tv.establecer_canal(5)
tv.apagar()

radio.encender()
radio.establecer_canal("98.5 FM")
radio.apagar()

# Funciones encender, establecer canal y apagar del DVD
dvd.encender()
dvd.establecer_canal("DVD player")
dvd.apagar()
