from funciones_alumnos import *
import time

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
    },

    {
                "nombre": "Carlos",
                "apellidos": "Enrique",
                "edad": 19,
                "carrera": "Inegenieria en datos",
                "grupo": "seccion 1",
                "calificacion": 5
    }

]   

"""Estructua del proyecto"""

def main():
    programa = True
    print("Bienvenido al analizador de tareas")
    while True:
        time.sleep(1.5)
        print('*' * 95)
        print("Estas son las opciones del analizador")
        print(''' 1: Mostrar a los alumnos
        2: Buscar al alumno
        3: Agregar alumno
        4: Modificar alumno
        5: Salir
''')    
    
        opcion_elegida = validar_opcion(input("Escoge el número de opción para realizar "))
        if not opcion_elegida:
            continue
                
        

        
        match opcion_elegida:
            
            case 1:
                print("Cargando...")
                time.sleep(1.5)
                mostrar_alumnos(alumnos)
                time.sleep(3)
            
            case 2:
                print("Cargando...")
                time.sleep(1.5)
                nombre_alumno = (input("Ingresa el nombre del alumno: ").lower()).capitalize()
                apellido_alumno = (input("Ingresa el apellido del alumno: ").lower()).capitalize()
                alumno = buscar_alumno(alumnos, nombre_alumno, apellido_alumno)
                if alumno:
                    print(f'{alumno["nombre"]:<16}|{alumno["apellidos"]:<21}|{alumno["edad"]:<5}|{alumno["carrera"]:<20}|{alumno["grupo"]:<16}|{alumno["calificacion"]:<5}')
                else:
                    print("El alumno no ha sido encontrado o no existe")
                time.sleep(3)
            
            case 3:
                nombre_alumno = (input("Ingresa el nombre del alumno: ").lower()).capitalize()
                apellido_alumno = (input("Ingresa el apellido del alumno: ").lower()).capitalize()
                edad_alumno = int(input("Ingresa la edad del alumno: "))
                carrera_alumno = (input("Ingresa la carrera del alumno: ").lower()).capitalize()
                grupo_alumno = (input("Ingresa el grupo del alumno: ").lower()).capitalize()
                calificacion_alumno = int(input("Ingresa la calificacion del alumno: "))
                agregar_alumno(alumnos, nombre_alumno, apellido_alumno, edad_alumno, carrera_alumno, grupo_alumno, calificacion_alumno)
                print("El alumno ha sido agregado exitosamente")
                time.sleep(3)


            case 4:
                nombre_alumno = input("Escoge el nombre del alumno que deseas modificar: ")
                apellido_alumno = input("Escoge el apellido del alumno que deseas modificar: ")
                alumno = buscar_alumno(alumnos, nombre_alumno, apellido_alumno)
                time.sleep(2)
                if alumno:
                        modificar_alumno(alumno)
                else:
                    print("El alumno no ha sido encontrado o no existe")


            case 5:
                break
            case _:
                print("Esa opción no es valida")

                
        

main()