#Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 090112.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from configuracion import cadena_base_datos

from crear_tablas import Establecimiento


engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

cont = 0

establecimientos = session.query(Establecimiento).filter(
    Establecimiento.codigo_distrito == "090112").order_by(
        Establecimiento.sostenimiento).all()

# establecimientos = session.query(Establecimiento).filter(
#    Establecimiento.codigo_distrito == "09D12").order_by(
#        Establecimiento.sostenimiento).all()


#PRESENTA TODOS LOS ESTABLECIMIENTOS
print("****Presentación de Establecimientos ordenados por sostenimiento****")
for e in establecimientos:
    print("Sostenimiento: %s\n Nombre establecimiento: %s\n Número de docentes: %d\nTipo de educación: %s\n Codigo distrito: %s\n" % (
        e.sostenimiento,
        e.nombre,
        e.numero_docentes,
        e.tipo_educacion,
        e.codigo_distrito))
    cont += 1

print(cont)


