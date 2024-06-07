# Los establecimientos que tienen como parte de nombre la cadena "UNIDOS".

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from configuracion import cadena_base_datos

from crear_tablas import Establecimiento


engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

establecimientos = session.query(Establecimiento).filter(Establecimiento.nombre.like("%UNIDOS%"))
cont = 0

for i in establecimientos:
    print("Nombre del establecimiento: %s \n Tipo de educación: %s\n" % (
        i.nombre,
        i.tipo_educacion
    ))
    cont += 1


print(cont)