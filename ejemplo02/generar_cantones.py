from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Canton, Provincia

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

archivo = open('data/Listado-Instituciones-Educativas-02.csv', 'r', encoding='utf-8')
lineas = archivo.readlines()
lineas = [l.split("|") for l in lineas]
lineas = lineas[1:]
lista = []

for l in lineas:
    lista.append((int(l[4]), l[5], int(l[2])))

lista = list(set(lista))

for linea in lista:
    provincia = session.query(Provincia).filter(Provincia.codigo==linea[2]).first()
    canton = Canton(codigo=linea[0], nombre=linea[1], provincia=provincia)
    session.add(canton)

archivo.close()
session.commit()
