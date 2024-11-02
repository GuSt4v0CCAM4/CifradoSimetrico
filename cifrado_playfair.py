def crear_matriz_clave(clave):
    clave = ''.join(sorted(set(clave.upper()), key=clave.index)).replace('J', 'I')
    alfabeto = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matriz = []
    for letra in clave + alfabeto:
        if letra not in matriz:
            matriz.append(letra)
    return [matriz[i:i + 5] for i in range(0, 25, 5)]

def preparar_texto(texto):
    texto = texto.upper().replace("J", "I").replace(" ", "")
    pares = []
    i = 0
    while i < len(texto):
        a = texto[i]
        b = texto[i + 1] if i + 1 < len(texto) else 'X'
        if a == b:
            pares.append(a + 'X')
            i += 1
        else:
            pares.append(a + b)
            i += 2
    return pares

def obtener_posicion(matriz, letra):
    for fila in range(5):
        for columna in range(5):
            if matriz[fila][columna] == letra:
                return fila, columna
    return None

def cifrar_pareja(matriz, par):
    fila1, col1 = obtener_posicion(matriz, par[0])
    fila2, col2 = obtener_posicion(matriz, par[1])

    if fila1 == fila2:
        return matriz[fila1][(col1 + 1) % 5] + matriz[fila2][(col2 + 1) % 5]
    elif col1 == col2:
        return matriz[(fila1 + 1) % 5][col1] + matriz[(fila2 + 1) % 5][col2]
    else:
        return matriz[fila1][col2] + matriz[fila2][col1]

def descifrar_pareja(matriz, par):
    fila1, col1 = obtener_posicion(matriz, par[0])
    fila2, col2 = obtener_posicion(matriz, par[1])

    if fila1 == fila2:
        return matriz[fila1][(col1 - 1) % 5] + matriz[fila2][(col2 - 1) % 5]
    elif col1 == col2:
        return matriz[(fila1 - 1) % 5][col1] + matriz[(fila2 - 1) % 5][col2]
    else:
        return matriz[fila1][col2] + matriz[fila2][col1]

def cifrar_playfair(texto, clave):
    matriz = crear_matriz_clave(clave)
    texto_preparado = preparar_texto(texto)
    texto_cifrado = [cifrar_pareja(matriz, par) for par in texto_preparado]
    return ''.join(texto_cifrado)

def descifrar_playfair(texto, clave):
    matriz = crear_matriz_clave(clave)
    texto_preparado = preparar_texto(texto)
    texto_descifrado = [descifrar_pareja(matriz, par) for par in texto_preparado]
    return ''.join(texto_descifrado)
