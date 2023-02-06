cadena1 = "hola55brisa"
cadena2 = "bienvenido"
# no todas las funciones son metodos, estos son funciones especificas de datos
# Dir es una funcion no un metodo, devuelve la lista de atributos válidos del objeto pasado
resultado = dir(cadena1)

# upper convierte todo a mayuscula
resultado1 = cadena1.upper()
# estructura de los metodos: DATO . METODO (parametro)

# lower convierte a minuscula
resultado2 = cadena2.lower()

# capitalize convierte la primera a mayuscula
resultado3 = cadena1.capitalize()

# Find-método encuentra la primera aparición del valor especificado, sino devuelve -1
# devuelve la posicion en la que se encuentra contando desde el 0
busqueda_find = cadena1.find("a")

# Index-método encuentra la primera aparición del valor especificado, sino devuelve una excepción
busqueda_index = cadena1.index("a")

# si es numerico, devuelve true, sino false
# aunque este entre comillas siendo un texto, busca numeros
es_numerico = cadena1.isnumeric()

# si es alfanumerico devuelve true, sino false
es_alfanumerico = cadena1.isalnum()  # el espacio no es alfanumerico

# si es alfabetico devuelve true
es_alfabetico = cadena1.isalpha()

# count buscamos una cadena en otra y devuelve el numero de veces que coincida
contar_coincidencias = cadena1.count("a")

# len, es una funcion, no un metodo, cuenta los caracteres de una cadena
contar_caracteres = len(cadena1)

# startswith verifica si una cadena comienza con otra cadena dada, si es asi devuelve true

comienza_con = cadena1.startswith("h")

# endswith verifica si una cadena termina con otra cadena, devuelve true
termina_con = cadena1.endswith("brisa")

# replace remplaza un valor por otro
cadena_nueva = cadena1.replace("la", "lu")

# split separa cadenas con la cadena que le pasemos, crea una lista
cadena_separada = cadena1.split(",")

# print(cadena_separada[1]) si hacemos esto nos va a mostrar el dato que hay en ese lugar de la lista que crea (maquina)

print(cadena_separada)
