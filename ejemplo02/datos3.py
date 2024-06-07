from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia, Canton
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

total = 0
suma=0
# canton_guayaquil = session.query(Canton).filter(Canton.nombre == "Guayaquil").one_or_none()

# if canton_guayaquil:
#     print("CANTÓN: %s, CÓDIGO: %d\n" % (canton_guayaquil.nombre, canton_guayaquil.codigo))
#     for parroquia in canton_guayaquil.parroquias:
#         establecimientos = parroquia.establecimientos        
#         for establecimiento in establecimientos:
#             print(" - ESTABLECIMIENTO: %s\n - TIPO DE EDUCACIÓN: %s\n" % (
#                 establecimiento.nombre,
#                 establecimiento.tipo_educacion
#             ))
#             total_establecimientos += 1
# else:
#     print("No se encontró el cantón de Guayaquil, no existe")

# print(total_establecimientos)

# session.close()


#Muestra el total de los docentes del canton "Isidro Ayora"
establecimientos = session.query(Establecimiento).join(Parroquia).join(Canton).filter(Canton.nombre == "Isidro Ayora").all()

for linea in establecimientos:
     print("Nombre: %s, Docentes: %s\n" % (linea.nombre, linea.numero_docentes))
     suma  += linea.numero_docentes
     total += 1
     
print("total numero docentes: %d" %(suma))
#con lista compresa
#establecimientos = sum([p.numero_docentes for p in session.query(Establecimiento).join(Parroquia).join(Canton).filter(Canton.nombre == "Isidro Ayora").all()])
#print(establecimientos)

session.close()