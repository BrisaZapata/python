ingreso_mensual = 81000
gasto_mensual = 80000

#if anidado y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print ("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print ("estas bien pa")
    else:
        print("y pa, estas gastando una banda")
elif ingreso_mensual > 1000:
    print ("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print ("estas bien en argentina")
else: 
    print("sos pobre")
#else + if = elif jeje sirve para poner muchas condiciones
