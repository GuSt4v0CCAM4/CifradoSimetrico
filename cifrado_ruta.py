def cifrar_por_ruta(mensaje, filas, columnas):
    # Crear una matriz vacía con el tamaño dado
    matriz = [['' for _ in range(columnas)] for _ in range(filas)]
    idx = 0

    for i in range(filas):
        for j in range(columnas):
            if idx < len(mensaje):
                matriz[i][j] = mensaje[idx]
                idx += 1

    mensaje_cifrado = ''
    for j in range(columnas):
        for i in range(filas):
            if matriz[i][j] != '':
                mensaje_cifrado += matriz[i][j]

    return mensaje_cifrado


def descifrar_por_ruta(mensaje_cifrado, filas, columnas):
    matriz = [['' for _ in range(columnas)] for _ in range(filas)]

    idx = 0
    for j in range(columnas):
        for i in range(filas):
            if idx < len(mensaje_cifrado):
                matriz[i][j] = mensaje_cifrado[idx]
                idx += 1

    mensaje_descifrado = ''.join(''.join(fila) for fila in matriz)

    return mensaje_descifrado
