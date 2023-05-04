#Escriba un programa que le solicite al usuario una cadena de caracteres en mayusculas e imprima una lista con cada palabra en minuscula
x = input ("ingresar una cadena de texto en mayuscula y minuscula") 
partes=  (x.lower().split())
print(" las palabras en minusculas son:", partes)