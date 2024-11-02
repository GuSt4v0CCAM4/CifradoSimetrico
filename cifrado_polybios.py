def cifrar_polybios(mensaje):
    alfabeto = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matriz = {alfabeto[i]: (i // 5 + 1, i % 5 + 1) for i in range(len(alfabeto))}
    mensaje_cifrado = ''
    for letra in mensaje.upper():
        if letra in matriz:
            fila, columna = matriz[letra]
            mensaje_cifrado += str(fila) + str(columna)
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

def descifrar_polybios(mensaje_cifrado):
    alfabeto = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matriz_inversa = {(i // 5 + 1, i % 5 + 1): alfabeto[i] for i in range(len(alfabeto))}
    mensaje_descifrado = ''
    i = 0

    while i < len(mensaje_cifrado):
        if mensaje_cifrado[i].isdigit() and i + 1 < len(mensaje_cifrado) and mensaje_cifrado[i + 1].isdigit():
            fila = int(mensaje_cifrado[i])
            columna = int(mensaje_cifrado[i + 1])
            if (fila, columna) in matriz_inversa:
                mensaje_descifrado += matriz_inversa[(fila, columna)]
            else:
                mensaje_descifrado += '?'
            i += 2
        else:
            mensaje_descifrado += mensaje_cifrado[i]
            i += 1

    return mensaje_descifrado
