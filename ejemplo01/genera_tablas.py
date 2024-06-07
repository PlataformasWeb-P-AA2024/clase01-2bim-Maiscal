from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
import datetime
# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()



# Ejemplo que representa la relación entre dos clases
# One to Many
# Un club tiene muchos jugadores asociados

class Club(Base):
    __tablename__ = 'club'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    deporte = Column(String(100))
    fundacion = Column(Integer, nullable=False)
    # Mapea la relación entre las clases
    # Club puede acceder a los jugadores asociados
    # por la llave foránea
    jugadores = relationship("Jugador", back_populates="club")

    
    def __repr__(self):
        return "Club: nombre=%s deporte=%s fundación=%d" % (
                          self.nombre, 
                          self.deporte, 
                          self.fundacion)

    def obtener_anios_vida(self):
        #presentamos los años de vida del club con datetime.
        return datetime.datetime.now().year - self.fundacion

    def obtener_dorsales_jugadores(self):
        #por medio del for llamamos a un objeto jugadores y para presentar
        #sin tener que presentar la lista presentamos una cadena
        cadena = ""
        lista = []
        for l in self.jugadores:
            lista.append(l.dorsal)
            cadena = "%s%d\n"%(cadena, l.dorsal)
        return cadena
        
    def obtener_suma_dorsales(self):
        #Aqui de la manera tradicional se puede presentar la lista utilizando varias lineas de codigo
        #suma = 0
        #for l in self.jugadores:
            #suma = suma + l.dorsal
        
        #Utilizamos listas compresas para poder sumar todo los dorsales en una sola linea.
        suma = sum([s.dorsal for s in self.jugadores])
        return suma
        #Ambos estan bien uno optimiza lineas y el otro no.

class Jugador(Base):
    __tablename__ = 'jugador'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    dorsal = Column(Integer)
    posicion = Column(String(100))
    # se agrega la columna club_id como ForeignKey
    # se hace referencia al id de la entidad club
    club_id = Column(Integer, ForeignKey('club.id'))
    # Mapea la relación entre las clases
    # Jugador tiene una relación con Club
    club  = relationship("Club", back_populates="jugadores")
    
    def __repr__(self):
        return "Jugador: %s - dorsal:%d - posición: %s" % (
                self.nombre, self.dorsal, self.posicion)

    def obtener_dorsales_jugadores(self):
        return self.dorsal


Base.metadata.create_all(engine)









