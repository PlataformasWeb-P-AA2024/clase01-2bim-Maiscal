from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Parroquia, Canton

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

archivo = open('data/Listado-Instituciones-Educativas-02.csv', 'r', encoding='utf-8')
lineas = archivo.readlines()
lineas = [l.split("|") for l in lineas]
lineas = lineas[1:]
lista = []

for l in lineas:
    lista.append((int(l[6]), l[7], int(l[4])))

lista = list(set(lista))

for linea in lista:
    canton = session.query(Canton).filter(Canton.codigo==linea[2]).first()

    parroquia = Parroquia(codigo=linea[0], nombre=linea[1], canton=canton)
    session.add(parroquia)

archivo.close()
session.commit()