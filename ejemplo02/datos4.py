from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia, Canton
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

total_establecimientos = 0

# cantones = session.query(Canton).filter(Canton.nombre.in_(["Urdaneta", "Vinces"])).all()

# for canton in cantones:
#     print("CANTÓN: %s, CÓDIGO: %d\n" % (canton.nombre, canton.codigo))
#     for parroquia in canton.parroquias:
#         establecimientos = parroquia.establecimientos
#         for establecimiento in establecimientos:
#             print(" - ESTABLECIMIENTO: %s\n - TIPO DE EDUCACIÓN: %s\n" % (
#                 establecimiento.nombre,
#                 establecimiento.tipo_educacion
#             ))
#             total_establecimientos += 1

# print(total_establecimientos)

#Muestra los establecimientos de los cantones Urdaneta y Vinces
establecimientos = session.query(Establecimiento).join(Parroquia).join(Canton).filter(Canton.nombre.in_(["Urdaneta", "Vinces"])).all()

for linea in establecimientos:
     print("Nombre: %s, Canton: %s\n" % (linea.nombre, linea.parroquia.canton.nombre))
     total_establecimientos += 1
     
print(total_establecimientos)

session.close()

