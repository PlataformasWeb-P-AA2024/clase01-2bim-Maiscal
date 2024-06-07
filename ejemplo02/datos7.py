# Los cantones que tiene establecimientos con 0 número de profesores y 210 estudiantes

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from configuracion import cadena_base_datos

from crear_tablas import Establecimiento, Parroquia, Canton


engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

cont = 0

cantones = session.query(Canton).all()

for canton in cantones:

    for parro in canton.parroquias:
        establecimientos = parro.establecimientos
        for esta in establecimientos:
            
            if esta.numero_docentes == 0 and esta.numero_estudiantes == 210:

                print("CANTÓN: %s\n" % (canton.nombre))
                print(" - ESTABLECIMIENTO: %s\n - TIPO DE EDUCACIÓN: %s\n" % (
                    esta.nombre,
                    esta.tipo_educacion
                ))
                cont += 1

print(cont)
session.close()