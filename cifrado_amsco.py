def cifrar_amsco(mensaje, clave):
    bloques = []
    alterna = True
    i = 0
    while i < len(mensaje):
        tamanio = 1 if alterna else 2
        bloques.append(mensaje[i:i+tamanio])
        i += tamanio
        alterna = not alterna

    num_columnas = len(clave)
    columnas = [[] for _ in range(num_columnas)]

    for idx, bloque in enumerate(bloques):
        columna = idx % num_columnas
        columnas[columna].append(bloque)

    columnas_ordenadas = [None] * num_columnas
    for idx, pos in enumerate(sorted(range(num_columnas), key=lambda k: clave[k])):
        columnas_ordenadas[idx] = ''.join(columnas[pos])

    mensaje_cifrado = ''.join(columnas_ordenadas)
    return mensaje_cifrado
def descifrar_amsco(mensaje_cifrado, clave):
    bloques = []
    alterna = True
    i = 0
    while i < len(mensaje_cifrado):
        tamanio = 1 if alterna else 2
        bloques.append(tamanio)
        i += tamanio
        alterna = not alterna

    num_columnas = len(clave)
    longitud_columnas = [0] * num_columnas
    for idx, bloque in enumerate(bloques):
        columna = idx % num_columnas
        longitud_columnas[columna] += bloque

    columnas = []
    pos = 0
    for longitud in sorted(range(num_columnas), key=lambda k: clave[k]):
        columnas.append(mensaje_cifrado[pos:pos + longitud_columnas[longitud]])
        pos += longitud_columnas[longitud]

    columnas_ordenadas = [None] * num_columnas
    for idx, pos in enumerate(sorted(range(num_columnas), key=lambda k: clave[k])):
        columnas_ordenadas[pos] = columnas[idx]

    mensaje_descifrado = ''
    i = 0
    alterna = True
    while i < len(mensaje_cifrado):
        for columna in columnas_ordenadas:
            if len(columna) == 0:
                continue
            tamanio = 1 if alterna else 2
            mensaje_descifrado += columna[:tamanio]
            columnas_ordenadas[i % num_columnas] = columna[tamanio:]
            i += tamanio
            alterna = not alterna

    return mensaje_descifrado
