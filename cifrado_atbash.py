def cifrar_atbash(mensaje):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabeto_invertido = alfabeto[::-1]
    mensaje_cifrado = ''
    for letra in mensaje.upper():
        if letra in alfabeto:
            mensaje_cifrado += alfabeto_invertido[alfabeto.index(letra)]
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado
