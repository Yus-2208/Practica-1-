x = input("ingresar tres numeros enteros separados por comas")
lista_1 = [int(x) for x in x.split(",")]
lista_1.sort()
# imprimimos la lista ordenada 
print("La lista ordenada es:", lista_1)