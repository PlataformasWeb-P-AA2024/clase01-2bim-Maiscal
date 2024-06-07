from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia, Canton, Provincia
from configuracion import cadena_base_datos
from sqlalchemy import or_

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

canton = session.query(Canton).all()
provincia = session.query(Provincia).all()
parroquia = session.query(Parroquia).all()




## - A cada cantón pedirle el número de estudiantes#####
for i in canton:
    print("-------Numero de estudiantes de un Canton--------")
    print("Canton: %s" % (i.nombre))
    print("Numero de estudiantes: %s" %(i.obtener_numero_estudiante()))
    print("---------------\n")

print("*****************************\n")


## - A cada provincia perdile el número de docentes#####
for i in provincia:
    print("-------Numero de docentes de una Provincia--------")
    print("Provincia: %s" % (i.nombre))
    print("Numero de docentes: %s" %(i.obtener_numero_docentes()))
    print("---------------\n")

print("*****************************\n")

## - A cada parroaquia preguntar el número de establecimientos####
for i in parroquia:
    print("-------Numero de establecimientos de una parroquia--------")
    print("Parroquia: %s" % (i.nombre))
    print("Numero de establecimientos: %s" %(i.obtener_numero_establecimientos()))
    print("---------------\n")


## - A cada provincia preguntar la lista de parroquias#####
print("*****************************\n")

for i in provincia:
    print("-------En una provincia preguntar lista de parroquias--------")
    print("Provincia: %s" % (i.nombre))
    print("%s" %(i.obtener_lista_parroquias()))
    print("---------------\n")



## - A cada parroquia preguntarle los tipos jornada de los establecimientos#####

print("*****************************\n")

for i in parroquia:
    print("-------En una parroquia preguntar tipos de jornadas--------")
    print("Parroquia: %s" % (i.nombre))
    print("%s" %(i.obtener_tipos_jornada_establecimiento()))
    print("---------------\n")