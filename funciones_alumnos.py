'''Funcion encargada de imprimir los alumnos en consola'''

def mostrar_alumnos(alumnos):
    print(f"{'Nombre Alumno':<16}|{'Apellidos alumno':<21}|{'Edad':<5}|{'Carrera':<20}|{'Grupo':<16}|{'Calificacion':<5}")
    print('*'*100)
    for alumno in alumnos:
      print(f'{alumno["nombre"]:<16}|{alumno["apellidos"]:<21}|{alumno["edad"]:<5}|{alumno["carrera"]:<20}|{alumno["grupo"]:<16}|{alumno["calificacion"]:<5}')


def buscar_alumno(alumnos,nombre, apellido):

    for alumno in alumnos:
       if nombre in alumno["nombre"] and apellido in alumno["apellidos"]:
          return alumno
    return False
         

def agregar_alumno(lista_alumnos,nombre, apellidos, edad, carrera, grupo, calificacion):
   alumno_nuevo = {
      'nombre': nombre,
      "apellidos": apellidos,
      "edad": edad,
      "carrera": carrera,
      "grupo": grupo,
      "calificacion": calificacion
   }
   lista_alumnos.append(alumno_nuevo)

def modificar_alumno(alumno): #se hara un llamado a buscar alumno, de ahí agregara como parametro al alumno

   listas_opciones = ['nombre', 'apellidos', 'edad', 'carrera','grupo','calificacion']
   print('Qué deseas modificar? nombre|apellidos|edad|carrera|grupo|calificacion')
   eleccion = input('')

   if eleccion in listas_opciones and eleccion not in ("edad","calificacion"):
      modificacion = input('Ingrese el nuevo valor: ')
      alumno[eleccion] = modificacion


   elif eleccion == "edad":
        while True:
         try:
          modificacion = validar_edad(input('Ingrese la edad: '))
          if modificacion is not (None): #si regresara un valor None entonces volveria a pedirte la calificacion
               alumno[eleccion] = modificacion
               break
         except ValueError:
                print("No has introducido un numero")
            
            



   elif eleccion == "calificacion":
        while True:
         try:
                modificacion = validar_calificacion(input('Ingrese la calificacion: '))
                if modificacion is not (None): #si regresara un valor None entonces volveria a pedirte la calificacion
                  alumno[eleccion] = modificacion
                  break
         except ValueError:
                print("No has introducido un numero")
         
      
   else:
      print("Has ingresado una opcion no valida")

def validar_opcion(opcion):
    try:
        opcion = int(opcion)
        if opcion in range(1,6):
            return opcion
        else:
            print("Por favor escoge un numero de opción válido")
    except ValueError:
         print("Esa eleccion no es válida, por favor ingresa el número de opción que deseas")

def validar_calificacion(calificacion):
      try:
          calificacion=int(calificacion)
          if calificacion in range (1,11):
              return calificacion
          else:
              print("numero no acorde al sistema de calificación(1-10)")
      except ValueError:
         print ("revise que el numero ingresado va acorde a los manejados en el sistema")

def validar_edad(edad):
      try:
         edad=int(edad)
         if edad in range (18,60):
             return edad
         else:
               print("Revise que la edad ingresada sea acorde al rango (18,60)")
      except ValueError:
         print ("Opcion no valida, revise el dato ingresado")
      