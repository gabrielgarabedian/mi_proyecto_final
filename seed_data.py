from ejemplo.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123, fecha_de_nacimiento="1994-08-19").save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890, fecha_de_nacimiento="1969-12-04").save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345, fecha_de_nacimiento="1991-06-25").save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567, fecha_de_nacimiento="2017-10-30").save()

print("Se cargo con éxito los usuarios de pruebas")