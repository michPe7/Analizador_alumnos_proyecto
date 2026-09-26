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

   if eleccion in listas_opciones and eleccion not in ("edad","calificacion"):
      modificacion = input('Ingrese el nuevo valor: ')
      alumno[eleccion] = modificacion


   elif eleccion == "edad":
        while True:
         try:
          modificacion = int(input('Ingrese la edad: '))
          if modificacion not in range(18,32):
                 print("Esa edad no es válida")
          else:
                alumno[eleccion] = modificacion
                break
         except ValueError:
                print("No has introducido un numero")


   elif eleccion == "calificacion":
        while True:
         try:
                modificacion = int(input('Ingrese la calificacion: '))
                if modificacion not in range(1,11):
                  print("Esa calificacion no es válida")

                else:
                  alumno[eleccion] = modificacion
                  break
         except ValueError:
                print("No has introducido un numero")
         
      
   else:
      print("Has ingresado una opcion no valida")

def validar_opcion(opcion):
    try:
        opcion = int(opcion)
        if opcion in range(1,5):
            return opcion
        else:
            print("Por favor escoge un numero de opción válido")
    except ValueError:
         print("Esa eleccion no es válida, por favor ingresa el número de opción que deseas")
