#Los establecimientos ordenados por número de profesores; 
#que tengan más de 100 profesores y régimen escolar igual Costa.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from configuracion import cadena_base_datos

from crear_tablas import Establecimiento


engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

establecimientos = session.query(Establecimiento).filter(and_(
        Establecimiento.regimen_escolar == "COSTA",
        Establecimiento.numero_docentes > 100)
).order_by(Establecimiento.numero_docentes.asc()).all()


#PRESENTAR LOS NOMBRES DE LOS ESTABLECIMIENTOS POR NUMERO DE DOCENTES
print("****Presentación de Establecimientos ordenados por número de profesores > 100 y régimen igual a COSTA****\n")
for e in establecimientos:
    print("Regimen: %s - Nombre establecimiento: %s - Numero de docentes: %d" % (
        e.regimen_escolar, 
        e.nombre, 
        e.numero_docentes
    ))

#print(len(establecimientos))