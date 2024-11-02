def cifrar_cesar(mensaje, desplazamiento):
    cifrado = ''
    for letra in mensaje:
        if letra.isalpha():
            desplazamiento_ascii = 65 if letra.isupper() else 97
            letra_cifrada = chr((ord(letra) - desplazamiento_ascii + desplazamiento) % 26 + desplazamiento_ascii)
            cifrado += letra_cifrada
        else:
            cifrado += letra
    return cifrado
def descifrar_cesar(mensaje, desplazamiento):
    descifrado = ''
    for letra in mensaje:
        if letra.isalpha():
            desplazamiento_ascii = 65 if letra.isupper() else 97
            letra_descifrada = chr((ord(letra) - desplazamiento_ascii - desplazamiento) % 26 + desplazamiento_ascii)
            descifrado += letra_descifrada
        else:
            descifrado += letra
    return descifrado