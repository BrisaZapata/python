# te amo mi amorrrrrrrrrrrrrrrrrrrrrrrr
# cada 1 segundo una persona normal dice 2 palabras
frase = input(
    "Decime una frase y te calculo cuanto tardarias si tuvieras que decirla ")

palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)

print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirla")

print(f"Dalto lo diria en {cantidad_de_palabras*100//2*0.7/100} segundos")

if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")
