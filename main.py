
#Es un comentario y es linea no sera ejecutada

#lee la variable y le asigna un valor y la guarda en memoria
nombre = input("Ingresa tu nombre: ") #imprime ms al usuario y espere que ingrese dato
apellido = input("Ingresa tu apellido: ") 
ciudad = input("Ingresa tu ciudad: ") 

print(f"Hola {nombre} {apellido}, Seleccionaste la ciudad: {ciudad}") #agregar f al inicio y variable entre key

nombreCompleto =f"{nombre} {apellido}"

print(f"Nombre completo {nombreCompleto}")
