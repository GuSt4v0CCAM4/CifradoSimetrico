import cifrado_atbash
import cifrado_ruta
import cifrado_amsco
import cifrado_cesar
import cifrado_playfair
import cifrado_polybios

def menu():
    while True:
        print("\n--- Menu de Cifrados Simetricos ---")
        print("1. Cifrado Cesar")
        print("2. Cifrado Atbash")
        print("3. Cifrado Playfair")
        print("4. Cifrado Polybios")
        print("5. Cifrado Amsco")
        print("6. Cifrado por Ruta")
        print("7. Salir")

        opcion = input("Selecciona un Cifrado Simetrico: ")

        if opcion == "1":
            print("--------------------")
            print("1.Cifrar")
            print("1.Descifrar")
            print("2. Volver a Menu")
            print("--------------------")
            opc = input("Selecciona una opcion: ")

            if opc == "1":
                mensaje = input("Ingrese el texto a cifrar:")
                desplazamiento = int(input("Ingrese el desplazamiento:"))
                resultado = cifrado_cesar.cifrar_cesar(mensaje, desplazamiento)
                print("Texto Cifrado:", resultado)

            elif opc == "2":
                mensaje = input("Ingrese el texto a descifrar:")
                desplazamiento = int(input("Ingrese el desplazamiento:"))
                resultado = cifrado_cesar.descifrar_cesar(mensaje, desplazamiento)
                print("Texto Descifrado:", resultado)
            elif opc == "3":
                break
            else:
                print("Opcion no valida")
        elif opcion == "2":
            print("--------------------")
            print("1.Cifrar")
            print("1.Descifrar")
            print("2. Volver a Menu")
            print("--------------------")
            opc = input("Selecciona una opcion: ")

            if opc == "1":
                mensaje = input("Ingrese el texto a cifrar:")
                resultado = cifrado_atbash.cifrar_atbash(mensaje)
                print("Texto Cifrado:", resultado)

            elif opc == "2":
                mensaje = input("Ingrese el texto a descifrar:")
                resultado = cifrado_atbash.cifrar_atbash(mensaje)
                print("Texto Descifrado:", resultado)
            elif opc == "3":
                break
            else:
                print("Opcion no valida")
        elif opcion == "3":
            print("--------------------")
            print("1.Cifrar")
            print("1.Descifrar")
            print("2. Volver a Menu")
            print("--------------------")
            opc = input("Selecciona una opcion: ")

            if opc == "1":
                mensaje = input("Ingrese el texto a cifrar:")
                clave = input("Ingrese la clave:")
                resultado = cifrado_playfair.cifrar_playfair(mensaje, clave)
                print("Texto Cifrado:", resultado)

            elif opc == "2":
                mensaje = input("Ingrese el texto a descifrar:")
                clave = input("Ingrese la clave:")
                resultado = cifrado_playfair.descifrar_playfair(mensaje, clave)
                print("Texto Descifrado:", resultado)
            elif opc == "3":
                break
            else:
                print("Opcion no valida")
        elif opcion == "4":
            print("--------------------")
            print("1.Cifrar")
            print("1.Descifrar")
            print("2. Volver a Menu")
            print("--------------------")
            opc = input("Selecciona una opcion: ")

            if opc == "1":
                mensaje = input("Ingrese el texto a cifrar:")
                resultado = cifrado_polybios.cifrar_polybios(mensaje)
                print("Texto Cifrado:", resultado)

            elif opc == "2":
                mensaje = input("Ingrese el texto a descifrar:")
                resultado = cifrado_polybios.descifrar_polybios(mensaje)
                print("Texto Descifrado:", resultado)
            elif opc == "3":
                break
            else:
                print("Opcion no valida")
        elif opcion == "5":
            print("--------------------")
            print("1.Cifrar")
            print("1.Descifrar")
            print("2. Volver a Menu")
            print("--------------------")
            opc = input("Selecciona una opcion: ")

            if opc == "1":
                mensaje = input("Ingrese el texto a cifrar:")
                clave = input("Ingrese la clave:")
                resultado = cifrado_amsco.cifrar_amsco(mensaje, clave)
                print("Texto Cifrado:", resultado)

            elif opc == "2":
                mensaje = input("Ingrese el texto a descifrar:")
                clave = input("Ingrese la clave:")
                resultado = cifrado_amsco.descifrar_amsco(mensaje, clave)
                print("Texto Descifrado:", resultado)
            elif opc == "3":
                break
            else:
                print("Opcion no valida")
        elif opcion == "6":
            print("--------------------")
            print("1.Cifrar")
            print("1.Descifrar")
            print("2. Volver a Menu")
            print("--------------------")
            opc = input("Selecciona una opcion: ")

            if opc == "1":
                mensaje = input("Ingrese el texto a cifrar:")
                filas = int(input("Ingrese el numero de filas:"))
                columnas = int(input("Ingrese el numero de columnas:"))
                resultado = cifrado_ruta.cifrar_por_ruta(mensaje, filas, columnas)
                print("Texto Cifrado:", resultado)

            elif opc == "2":
                mensaje = input("Ingrese el texto a descifrar:")
                filas = int(input("Ingrese el numero de filas:"))
                columnas = int(input("Ingrese el numero de columnas:"))
                resultado = cifrado_ruta.descifrar_por_ruta(mensaje, filas, columnas)
                print("Texto Descifrado:", resultado)
            elif opc == "3":
                break
            else:
                print("Opcion no valida")
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    menu()

