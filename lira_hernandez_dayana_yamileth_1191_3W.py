print (" ") #espacio a agregar
print ("Lira Hernandez Dayana Yamileth:") #imprime datos del realizador
print (" ") #espacio agregar
print ("Determina cual de los numeros agregados es mayo o menor")
print (" ") #espacio agregar

a = int(input("Ingrese un numero (a):")) #instruccion para agregar numero
b = int(input("Ingrese un numero (b):")) #instruccion para agregar numero
c = int(input("Ingrese un numero (c):")) #instruccion para agregar numero

if a == b or a == c or b == c: #if inicia funciones verdaderas o falsas
    print("Error, los numeros no pueden ser iguales") #imprime si es verdad o falso
else: #else indica si la funcion es falsa o verdadera
        # Determinar el mayor y el menor
        mayor = a
        menor = a

        if b > mayor: #if indica funcion verdadera o falsa
            mayor = b #muestra el dato ingresado
        if c > mayor: #if indica funcion verdadera o falsa
            mayor = c #muestra el dato ingresado

        if b < menor: #if indica funcion verdadera o falsa
            menor = b #muestra el dato ingresado
        if c < menor: #if indica funcion verdadera o falsa
            menor = c #muestra el dato ingresado

        print("El mayor es:", mayor) # Imprime resultados
        print("El menor es:", menor) # Imprime resultados

print (" ")#imprime espacio a agregar