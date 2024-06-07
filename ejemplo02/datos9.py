# Los establecimientos ordenados por nombre de parroquia que 
# tengan más de 40 profesores y la cadena "Educación regular" 
# en tipo de educación.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from configuracion import cadena_base_datos

from crear_tablas import Establecimiento, Parroquia


engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

parroquias = session.query(Parroquia).order_by(
        Parroquia.nombre.asc()).all()

cont = 0

for pa in parroquias:
    
    establecimientos = session.query(Establecimiento).filter(and_(
        Establecimiento.parroquia_id == pa.id ,
        Establecimiento.numero_docentes > 40 ,
        Establecimiento.tipo_educacion == "Educación regular")).all()
    

    if establecimientos:
        print("------------------------------")
        print("** Parroquia: %s **\n" % (pa.nombre))
        
        for es in establecimientos:
            print("Nombre establecimiento: %s - Número de docentes: %d - Tipo de educación: %s" % (
                es.nombre,
                es.numero_docentes,
                es.tipo_educacion
                ))
            cont += 1

print(cont)