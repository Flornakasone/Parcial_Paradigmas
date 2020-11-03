import csv
import os.path


def carga_datos(campos):
    nombre_archivo = input("Ingrese nombre para el archivo(con la extension '.csv'): ")
    
    guardar = "si"
    legajo_empleados = []
    while guardar == "si":
        empleado = {}    
        for campo in campos: 
            empleado[campo] = input(f"Ingrese {campo} del empleado: ")
            legajo_empleados.append(empleado)
        guardar = input("Desea seguir ingresando datos? si/no: ")
        return legajo_empleados

    try:
        archivo_existe = os.path.isfile(nombre_archivo)
        if archivo_existe:
            print("Ese archivo ya existe")
            modif_archivo = input("Desea escribir o modificar el archivo?: \n 1. Modificar \n 2. Sobreescribir \n ")
            
            if modif_archivo == "1":
                with open(nombre_archivo, "a") as f:
                    entrada_csv = csv.DictWriter(f, fieldnames=campos)
            if modif_archivo == "2":
                with open(nombre_archivo, "w") as f:
                    entrada_csv = csv.DictWriter(f, fieldnames=campos) 
            if not archivo_existe :
                entrada_csv.writeheader()
            entrada_csv.writerows(legajo_empleados)
            print("Guardando datos...")   
              
    except IOError:
        print("Hubo un error, no se puede visualizar el archivo") 

def estado_vacaciones(registro, legajo):
    try:
        with open(registro) as f_registro, open(legajo) as f_legajo:
            registro_csv = csv.DictReader(f_registro) #leemos
            legajo_csv = csv.DictReader(f_legajo) #leemos

            # Empieza a leer desde la primer linea
            legajo = next(legajo_csv, None)
            registro = next(registro_csv, None)

            while legajo: #mientras no sea vacia
                if not registro or registro["Legajo"] != legajo["Legajo"]:
                    print(f"El legajo {legajo['Legajo']} no se encuentra  en nuestro registro") 
                while registro and registro["Legajo"] == legajo["Legajo"]:
                    print(f"De los {legajo['Total Vacaiones']} le quedan {legajo['Total de Vacaciones'] - registro[3]} ") 
                    registro= next(registro_csv, None)
                legajo = next(legajo_csv, None)
    except IOError:
        print("Hubo un error, no se puede visualizar el archivo") 


#a
def menu():
    ARCHIVO = "registro_vacaciones.csv"
    CAMPOS = ["Legajo", "Apellido", "Nombre", "Total Vacaciones"]


    while True:
        
        print("Elija una opcion del Menu: \n 1. Cargar datos \n 2. Recuperar datos \n 3. Salir")
        opcion = input("")

        if opcion == "1":
            carga_datos(CAMPOS)
        if opcion == "2":
            estado_vacaciones(ARCHIVO, )
        if opcion == "3":
            print("Ha salido del programa")
            exit()    
        else:
            print("Elija una opcion valida")

menu()