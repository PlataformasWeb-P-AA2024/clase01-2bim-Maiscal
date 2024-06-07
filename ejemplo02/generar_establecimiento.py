from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

archivo = open('data/Listado-Instituciones-Educativas-02.csv', 'r', encoding='utf-8')
lineas = archivo.readlines()
lineas = [l.split("|") for l in lineas]
lineas = lineas[1:]
lista=[]

for l in lineas:
    lista.append((
        l[0], 
        l[1], 
        int(l[6]),
        l[8], 
        l[9], 
        l[10], 
        l[11], 
        l[12],
        l[13], 
        l[14], 
        l[15], 
        l[16], 
        l[17], 
        l[18], 
        l[19], 
        l[20], 
        int(l[21]), 
        int(l[22]), 
        l[23]))

lista = list(set(lista))

for linea in lista:
    parroquia = session.query(Parroquia).filter(Parroquia.codigo==linea[2]).first()
    
    establecimiento = Establecimiento(
        codigo_amie=linea[0],
        nombre=linea[1],
        parroquia=parroquia,
        zona_administrativa=linea[3],
        denominacion_distrito=linea[4],
        codigo_distrito=linea[5],
        codigo_circuito_educativo=linea[6],
        sostenimiento=linea[7],
        regimen_escolar=linea[8],
        jurisdiccion=linea[9],
        tipo_educacion=linea[10],
        modalidad=linea[11],
        jornada=linea[12],
        nivel=linea[13],
        etnia=linea[14],
        acceso=linea[15],
        numero_estudiantes=int(linea[16]),
        numero_docentes=int(linea[17]),
        estado=linea[18]
    )
    session.add(establecimiento)

archivo.close()
session.commit()

