#Zona de clases y metodos:

from datetime import datetime
import unittest

class Ruta:
    def __init__(self):
        self.puntos = []


class Punto:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud


class Camión:
    def __init__(self, placa, equipo):
        self.placa = placa
        self.equipo = equipo
        self.carga = Carga()


class Turno:
    def __init__(self, camion, ruta, horaInicio, horaFin):
        self.camion = camion
        self.ruta = ruta
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.ubicaciones = []

    def getGlass(self):
        total_glass = 0.0
        for ubicacion in self.ubicaciones:
            total_glass += ubicacion.carga.vidrio
        return total_glass


class Ubicación:
    def __init__(self, punto, tiempo):
        self.punto = punto
        self.tiempo = tiempo
        self.carga = Carga()


class Persona:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id


class Equipo:
    def __init__(self, conductor, asistente1, asistente2):
        self.conductor = conductor
        self.asistente1 = asistente1
        self.asistente2 = asistente2


class Carga:
    def __init__(self):
        self.vidrio = 0.0
        self.papel = 0.0
        self.plastico = 0.0
        self.metal = 0.0
        self.organicos = 0.0


class CentroAcopio:

    def __init__(self):
        self.registros = []

    def getGlassTotal(self, day):
        total_vidrio = 0.0
        for turno in self.registros:
            if turno.horaInicio.date() == day.date():
                total_vidrio += turno.getGlass()
        return total_vidrio


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.servicioRecoleccion = ServicioRecoleccion()
        self.centroAcopio = CentroAcopio()


class ServicioRecoleccion:
    def __init__(self):
        self.rutas = []
        self.camiones = []


#zona de instanciamiento de clases y definicion de valores necesarios para la ejecución del codigo (prueba de integración):


# Creación de objetos Persona
persona_conductor = Persona(nombre="Juan", id=1)
persona_asistente1 = Persona(nombre="Pedro", id=2)
persona_asistente2 = Persona(nombre="María", id=3)

# Creación de objeto Equipo
equipo = Equipo(conductor=persona_conductor, asistente1=persona_asistente1, asistente2=persona_asistente2)

# Creación de objeto Camión
camion = Camión(placa=1234, equipo=equipo)

# Creación de objeto Punto
punto1 = Punto(latitud=123, longitud=456)
punto2 = Punto(latitud=789, longitud=1011)

# Creación de objeto Ruta y asignación de puntos
ruta = Ruta()
ruta.puntos.append(punto1)
ruta.puntos.append(punto2)

# Creación de objetos Ubicación
tiempo1 = datetime.now()
ubicacion1 = Ubicación(punto=punto1, tiempo=tiempo1)
ubicacion2 = Ubicación(punto=punto2, tiempo=tiempo1)

# Asignación de carga a las ubicaciones
ubicacion1.carga.vidrio = 1.4
ubicacion2.carga.vidrio = 1
# la cantidad final ha de ser 2.4 (en este caso)

# Creación de objeto Turno y asignación de camión, ruta y ubicaciones
horaInicio = datetime.now()
horaFin = datetime.now()
turno = Turno(camion=camion, ruta=ruta, horaInicio=horaInicio, horaFin=horaFin)
turno.ubicaciones.append(ubicacion1)
turno.ubicaciones.append(ubicacion2)

# Creación de objeto CentroAcopio y registro del turno
centro_acopio = CentroAcopio()
centro_acopio.registros.append(turno)

# Creación de objeto Empresa y asignación de servicio de recolección y centro de acopio
empresa = Empresa(nombre="TrashCity")
empresa.servicioRecoleccion = ServicioRecoleccion()
empresa.centroAcopio = centro_acopio

# prueba con el unittest del metodo getGlassTotal, y a su vez internamente se evalua el getGlass por turno


class TestCentroAcopio(unittest.TestCase):
    def test_getGlassTotal(self):
        day = datetime(year=2023, month=5, day=19)
        total_vidrio = empresa.centroAcopio.getGlassTotal(day)
        expected_result = 2.4
        self.assertEqual(total_vidrio, expected_result)


if __name__ == '__main__':
    unittest.main()

# La misma modalidad de prueba pero de forma "manual" para ver la salida que da el metodo


day = datetime(year=2023, month=5, day=19)  
total_vidrio = empresa.centroAcopio.getGlassTotal(day)
print("Resultado de la prueba de integración: ")
print("El total de vidrio recolectado durante el dia ", day, "fue de: ", total_vidrio, "Ton")
print("El esperado como ya comprobo el unittest.")
