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
    }
]   

"""Estructua del proyecto"""

def main():
    programa = True
    while True:
        print("Bienvenido al analizador de tareas")
        time.sleep(1.5)
        print('*' * 95)
        print("Estas son las opciones del analizador")
        print(''' 1: Mostrar a los alumnos
        2: Buscar al alumno
        3: Agregar alumno
        4: Modificar alumno
''')
        opcion_elegida = validar_opcion(input("Escoge el número de opción para realizar "))
        match opcion_elegida:
            case 1:
                print("Cargando...")
                time.sleep(1.5)
                mostrar_alumnos(alumnos)
            

main()