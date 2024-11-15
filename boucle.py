# 1. Imprimir números de l’1 al 10 (amb for i amb while)
for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1
# 2. Sumar els primers 10 números utilitzant for i range().
suma  = 0
for x in range (1,11):
    suma = suma +x 
    print(suma)

# 3. Imprimir els elements d'una llista amb for.
fruits = ["poma","pera","raïm","plàtan"]
for i in fruits:
    print(i)

# 4. Imprimir els números parells i els imparells continguts en la següent llista.
num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]
for n in num:
    if n % 2 == 0:
        print(f"parells: {n}")
    else:
        print(f"imparells: {n}")

# 5. Sumar números parells i imparells.
suma_parells = 0
suma_imparells = 0
for n in num:
    if n % 2 == 0:
        suma_parells += n
    else:
        suma_imparells += n
print(f"La suma de los números pares es: {suma_parells}")
print(f"La suma de los números impares es: {suma_imparells}")

# 6. Sumar números fins a arribar a 100 amb while.
suma = 0
i = 0
while suma < 100:
    suma += i
    i += 1
print(suma)

nombre = 250  # Exemple: vous pouvez changer la valeur
while 100 <= nombre <= 400:
    print(f"el número {nombre} está comprendido entre 100 y 400")
    break