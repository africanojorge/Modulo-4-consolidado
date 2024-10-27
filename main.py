# main.py
from vehiculo import *
import csv

# Método para guardar datos en un archivo CSV
def guardar_datos_csv(vehiculos, nombre_archivo='vehiculos.csv'):
    try:
        with open(nombre_archivo, mode='w', newline='') as archivo:
            escritor = csv.writer(archivo)
            for vehiculo in vehiculos:
                escritor.writerow([vehiculo.__class__, vehiculo.__dict__])
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Método para leer datos desde un archivo CSV
def leer_datos_csv(nombre_archivo='vehiculos.csv'):
    try:
        with open(nombre_archivo, mode='r') as archivo:
            lector = csv.reader(archivo)
            for linea in lector:
                print(f"Lista de {linea[0].split('.')[-1][:-2]} {linea[1]}")
    except Exception as e:
        print(f"Error al leer los datos: {e}")

# Función principal con un menú interactivo
def menu():
    vehiculos = []
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear vehículos")
        print("2. Guardar en CSV")
        print("3. Leer desde CSV")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            tipo = input("Ingrese tipo (Particular, Carga, Bicicleta, Motocicleta): ").strip().lower()
            if tipo == "particular":
                vehiculos.append(Particular(
                    input("Marca: "), input("Modelo: "), input("Nro Ruedas: "),
                    input("Velocidad: "), input("Cilindrada: "), input("Nro Puestos: ")
                ))
            elif tipo == "carga":
                vehiculos.append(Carga(
                    input("Marca: "), input("Modelo: "), input("Nro Ruedas: "),
                    input("Velocidad: "), input("Cilindrada: "), input("Carga (Kg): ")
                ))
            elif tipo == "bicicleta":
                vehiculos.append(Bicicleta(
                    input("Marca: "), input("Modelo: "), input("Nro Ruedas: "), input("Tipo: ")
                ))
            elif tipo == "motocicleta":
                vehiculos.append(Motocicleta(
                    input("Marca: "), input("Modelo: "), input("Nro Ruedas: "),
                    input("Tipo: "), input("Motor: "), input("Cuadro: "), input("Nro Radios: ")
                ))
            else:
                print("Tipo de vehículo no válido.")
        elif opcion == '2':
            guardar_datos_csv(vehiculos)
        elif opcion == '3':
            leer_datos_csv()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú principal
if __name__ == '__main__':
    menu()

