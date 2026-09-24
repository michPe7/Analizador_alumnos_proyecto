'''Funcion encargada de imprimir los alumnos en consola'''

def mostrar_alumnos(alumnos):
    print(f'{'Nombre Alumno':<16}|{'Apellidos alumno':<21}|{'Edad':<5}|{'Carrera':<20}|{'Grupo':<16}|{'Calificacion':<5}')
    print('*'*100)
    for alumno in alumnos:
      print(f'{alumno["nombre"]:<16}|{alumno["apellidos"]:<21}|{alumno["edad"]:<5}|{alumno["carrera"]:<20}|{alumno["grupo"]:<16}|{alumno["calificacion"]:<5}')


def buscar_alumno(alumnos,nombre, apellido):

    for alumno in alumnos:
       if nombre in alumno["nombre"] and apellido in alumno["apellidos"]:
          return alumno
    return False
         

def agregar_alumno(lista_alumnos,nombre, apellidos, edad, carrera, grupo):
   alumno_nuevo = {
      'nombre': nombre,
      "apellidos": apellidos,
      "edad": edad,
      "carrera": carrera,
      "grupo": grupo,
      "calificacion": 0
   }
   lista_alumnos.append(alumno_nuevo)

def modificar_alumno(alumno): #se hara un llamado antes a buscar alumno y como devolvera el dict entonces sabre que hacer
   listas_opciones = ['nombre', 'apellidos', 'edad', 'carrera','grupo','calificacion']
   print('Qué deseas modificar? nombre|apellidos|edad|carrera|grupo|calificacion')
   eleccion = input('')
   if eleccion in listas_opciones:
      modificacion = input('Ingrese el nuevo valor: ')
      alumno[eleccion] = modificacion
   else:
      print("Has ingresado una opcion no valida")


alumnos = [
    {
        "nombre": "Michell",
        "apellidos": "Peralta Reyes",
        "edad": 18,
        "carrera": "Inegenieria en datos",
        "grupo": "seccion 2",
        "calificacion": 10
    },
    {
            "nombre": "Janet Itzel",
            "apellidos": "Lara Santiz",
            "edad": 18,
            "carrera": "Inegenieria en datos",
            "grupo": "seccion 3",
            "calificacion": 9
    },
    {
            "nombre": "Lizandro",
            "apellidos": "Gomez Vera",
            "edad": 20,
            "carrera": "Inegenieria en redes",
            "grupo": "605",
            "calificacion": 10
    },
    {
            "nombre": "Joseph",
            "apellidos": "Lopez Luis",
            "edad": 18,
            "carrera": "Gastronomia",
            "grupo": "G17",
            "calificacion": 8
    },
    {
            "nombre": "Carlos Sayed",
            "apellidos": "Villagomez Sanchez",
            "edad": 18,
            "carrera": "Inegenieria en datos",
            "grupo": "seccion 1",
            "calificacion": 7
    }
]   

print(mostrar_alumnos(alumnos))
alumno = buscar_alumno(alumnos=alumnos,nombre="Michell", apellido='Peralta')
modificar_alumno(alumno)
print(mostrar_alumnos(alumnos))