from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

total_establecimientos = 0
#
parroquias = session.query(Parroquia).join(Establecimiento).filter(Establecimiento.jornada == "Nocturna").all()

for linea in parroquias:
     print(linea.nombre)

     total_establecimientos += 1
     
print(total_establecimientos)

session.close()
