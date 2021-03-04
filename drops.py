def drops(numero):
    # variable de tipo string vacia para poder anidar los resultados
    resultado = ""
    if numero % 3 == 0:
        resultado += "Plic"
    if numero % 5 == 0:
        resultado += "Plac"
    if numero % 7 == 0:
        resultado += "Ploc"
    if numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
        resultado = numero
    return resultado


# Se convierte el input en un caracter de tipo entero para la validacion en
# los condicionales
print(drops(int(input("Introduce numero: "))))
