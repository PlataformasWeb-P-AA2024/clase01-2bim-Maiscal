# Los cantones que tiene establecimientos como número de estudiantes tales como: 1, 74, 100

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from configuracion import cadena_base_datos

from crear_tablas import Establecimiento, Parroquia, Canton


engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

cont = 0

establecimientos = session.query(Establecimiento).filter(or_(
    Establecimiento.numero_estudiantes == 1 , Establecimiento.numero_estudiantes == 74 , Establecimiento.numero_estudiantes == 100)).all()

for e in establecimientos:
    canton = e.parroquia.canton
    print("CANTÓN: %s\n" % (canton.nombre))
    print(" - Establecimiento: %s\n - Tipo de educacion: %s\n - Docentes: %d\n - Estudiantes: %d\n" % (
        e.nombre,
        e.tipo_educacion,
        e.numero_docentes,
        e.numero_estudiantes
        ))
    cont += 1

print(cont)
session.close()