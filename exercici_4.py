
salari = 55000
if salari < 15000:
    print(f"si el salary es {salari} IVA es 0%")
elif salari < 30000:
    iva = salari * 10 / 100
    print(f"si el salario es {salari}, el IVA es {iva}")
elif salari < 60000:
    iva = salari * 21 / 100
    print(f"si el salario es {salari}, el IVA es {iva}")
