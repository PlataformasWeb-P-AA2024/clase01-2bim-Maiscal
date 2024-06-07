from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia, Canton, Provincia
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

total_establecimientos = 0

provincia_bolivar = session.query(Provincia).filter(Provincia.nombre == "Bolivar").one()

if provincia_bolivar:
    print("PROVINCIA: %s, CODIGO: %d\n" % (provincia_bolivar.nombre, provincia_bolivar.codigo))
    for canton in provincia_bolivar.cantones:
        for parroquia in canton.parroquias:
            establecimientos = parroquia.establecimientos
            for establecimiento in establecimientos:
                print(" - ESTABLECIMIENTO: %s\n - TIPO DE EDUCACIÓN: %s\n" % (
                    establecimiento.nombre,
                    establecimiento.tipo_educacion
                ))
                total_establecimientos += 1


print(total_establecimientos)

session.close()
