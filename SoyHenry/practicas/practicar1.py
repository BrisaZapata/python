
    
variable1 = int (input ("ingresa un numero "))
variable2 = int (input ("ingresa un numero ")) 
variable3 = input ("ingrese una operacion (SUMA, RESTA, MULTIPLICACION,DIVISION) ")

if variable3 == "SUMA":
    print (variable1+variable2)
elif variable3 == "RESTA":
    print (variable1-variable2)
elif variable3 == "MULTIPLICACION":
    print(variable1*variable2)
elif variable3 == "DIVISION":
    print(variable1/variable2)
else:
    print("sos tonto")
