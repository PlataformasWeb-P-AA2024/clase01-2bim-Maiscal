from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=False)
    nombre = Column(String(100), nullable=False)
    cantones = relationship("Canton", back_populates="provincia")
    
    def __repr__(self):
        return "Provincia: codigo=%d - nombre=%s" % ( 
            self.codigo, 
            self.nombre)

    def obtener_numero_docentes(self):
        suma = 0
        for canton in self.cantones:
            for parroquia in canton.parroquias:
                for establecimiento in parroquia.establecimientos:
                    suma = suma + establecimiento.numero_docentes
        return suma
    
    def obtener_lista_parroquias(self):   
        cadena = ""
        for c in self.cantones:
            for p in c.parroquias:
                cadena = "%s%s\n" % (cadena, p.nombre)
        return cadena            

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=False)
    nombre = Column(String(100), nullable=False)
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")
    
    def __repr__(self):
        return "Canton: codigo=%d - nombre=%s - provincia_id=%d" % ( 
            self.codigo, 
            self.nombre, 
            self.provincia_id)

    def obtener_numero_estudiante(self):       
        suma = 0
        for i in self.parroquias:
            for p in i.establecimientos:
                suma = suma + p.numero_estudiantes
        return suma
        

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=False)
    nombre = Column(String(100), nullable=False)
    canton_id = Column(Integer, ForeignKey('canton.id'))
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos = relationship("Establecimiento", back_populates="parroquia")
    
    def __repr__(self):
        return "Parroquia: codigo=%d - nombre=%s - canton_id=%d" % (
            self.codigo, 
            self.nombre, 
            self.canton_id)

    def obtener_numero_establecimientos(self):
        cont = 0
        for l in self.establecimientos:
            cont = cont + 1
        return cont

    def obtener_tipos_jornada_establecimiento(self):
        jornadas = []
        for i in self.establecimientos:
            jornadas.append(i.jornada)
        return jornadas


class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigo_amie = Column(String(20), nullable=False)
    nombre = Column(String(100), nullable=False)
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    parroquia = relationship("Parroquia", back_populates="establecimientos")
    zona_administrativa = Column(String(50))
    denominacion_distrito = Column(String(100))
    codigo_distrito = Column(String(20))
    codigo_circuito_educativo = Column(String(20))
    sostenimiento = Column(String(50))
    regimen_escolar = Column(String(50))
    jurisdiccion = Column(String(50))
    tipo_educacion = Column(String(50))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    nivel = Column(String(50))
    etnia = Column(String(50))
    acceso = Column(String(50))
    numero_estudiantes = Column(Integer)
    numero_docentes = Column(Integer)
    estado = Column(String(20))
    
    def __repr__(self):
        return ("Establecimiento: codigo_amie=%s - nombre=%s - parroquia_id=%d - zona_administrativa=%s - "
                "denominacion_distrito=%s - codigo_distrito=%s - codigo_circuito_educativo=%s - sostenimiento=%s - "
                "regimen_escolar=%s - jurisdiccion=%s - tipo_educacion=%s - modalidad=%s - jornada=%s - nivel=%s - "
                "etnia=%s - acceso=%s - numero_estudiantes=%d - numero_docentes=%d - estado=%s") % (
                    self.codigo_amie, 
                    self.nombre, 
                    self.parroquia_id, 
                    self.zona_administrativa,
                    self.denominacion_distrito, 
                    self.codigo_distrito, 
                    self.codigo_circuito_educativo, 
                    self.sostenimiento,
                    self.regimen_escolar, 
                    self.jurisdiccion, 
                    self.tipo_educacion, 
                    self.modalidad, 
                    self.jornada, 
                    self.nivel,
                    self.etnia, 
                    self.acceso, 
                    self.numero_estudiantes, 
                    self.numero_docentes, 
                    self.estado)

Base.metadata.create_all(engine)
