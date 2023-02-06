# promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# diferencias de duracion

diferencias_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_con_max = 100 - dalto_curso * \
    1000 // otros_cursos_max / 10  # de esta forma corremos la ,
diferencias_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

# calculando el porcentaje de material inservible que se reduce
reducido_promedio = 100-otros_cursos_promedio*1000//crudo_promedio/10
reducido_dalto = 100-dalto_curso*1000//crudo_dalto/10

# mostrando las diferencias de duracion (ejercicio A)
print("-------------------")
print("El curso de Dalto dura: ")
print(
    f' - {diferencias_con_min}% menos que el mas rapido')
print(
    f' - {diferencias_con_max}% menos que el mas lento')
print(
    f' - {diferencias_con_promedio}% menos que el mas promedio')
print("-------------------")
# mostrando la cantidad de espacios vacios que se remueven (ejercicio B)

print(f'Un curso promedio elimina un {reducido_promedio}% de tiempo vacio')
print(f'Este curso elimina un {reducido_dalto}% de tiempo vacio')
print("-------------------")
# mostrando diferencias si los cursos duraran 10 horas

print(
    f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(
    f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso")
print("-------------------")
# /n es lo mismo que un enter
