from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia
from configuracion import cadena_base_datos
from sqlalchemy import or_

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

total_establecimientos = 0

parroquias = session.query(Parroquia).filter(or_(Parroquia.codigo == 20151, Parroquia.codigo == 20153)).all()

for parroquia in parroquias:
    print("---------------------------------------------------------------------------------------------")
    print("Parroquia: %s, codigo: %d\n" % (parroquia.nombre, parroquia.codigo))
    
    establecimientos = parroquia.establecimientos
    for establecimiento in establecimientos:
        print(" -ESTABLECIMIENTO: %s\n -TIPO DE EDUCACIÓN: %s\n" % (
            establecimiento.nombre, 
            establecimiento.tipo_educacion))
        total_establecimientos += 1
        
print(total_establecimientos)

session.close()