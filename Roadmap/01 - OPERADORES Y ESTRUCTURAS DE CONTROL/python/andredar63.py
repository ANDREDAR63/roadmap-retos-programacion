# operadores
"""
"""
# operadores aritmeticos
print (f"suma =10 + 3 ={10 + 3}")
print (f"resta =10 - 3 ={10 - 3}")
print (f"modulo =10 - 3 ={10 % 3}")
print (f"multiplicacion 10 * 3 ={10 * 3}")
print (f"division =10 / 3 ={10 / 3}")
print (f"exponenciacion =10 ** 3 ={10 ** 3}")
print (f"division baja =10 // 3 ={10 // 3}")

#operadores de comparacion

print (f"igualdad 10 == 3 es {10 == 3}")
print (f"desigualdad 10 != 3 es {10 != 3}")
print (f"mayor que 10 > 3 es {10 > 3}")
print (f"menor que 10 < 3 es {10 < 3}")
print (f"mayor o igual que 10 >= 3 es {10 >= 3}")
print (f"menor o igual que 10 <= 3 es {10 <= 3}")

#operadores logicos
print (f"and &&: 10 +3 = 13 and 5-1 == 4 es {10 + 3 == 13 and 5 - 1 == 4 }")
print (f"or ||: 10 +3 = 13 or 5-1 == 4 es {10 + 3 ==13 or 5 - 1 == 4  }")
print (f"not !: 10 +3 = 13 not 5-1 == 4 es {not 10 + 3 == 13}")

 #operadores de asignacion
my_number = 11 #el simbolo = es un operador para asignar una variable a "my_number"
print (f"# asignado {my_number}")
my_number += 1 #el simbolo += es un operador para asignar y sumar 
print (f"suma {my_number}")
my_number -= 1 #el simbolo -= es un operador para asignar y restar 
print (f"resta {my_number}")
my_number *= 2 #el simbolo *= es un operador para asignar y multiplicar 
print (f"multiplicacion {my_number}")
my_number /= 2 #el simbolo /= es un operador para asignar y dividir 
print (f"division {my_number}")
my_number %= 2 #el simbolo %= es un operador para asignar y modulo 
print (f"modulo {my_number}")
my_number **= 1 #el simbolo **= es un operador para asignar y exponer 
print (f"exponente {my_number}")
my_number //= 1 #el simbolo //= es un operador para asignar y realizar una division baja  
print (f"division baja {my_number}")

#operadores de identidad
my_new_number = my_number
print (f"my_number is my_new_number es {my_number is my_new_number}")

#operadores de pertenencia
print (f"'u' in 'mourodev = {'u' in 'mourodev'}")
print (f"'u' not in 'mourodev = {'u' not in 'mourodev'}")

#operadores de bit

a = 10 # transforma valores a bits
b = 3 #0011
print(f"AND: 10 & 3 ={10 & 3}") # 0010
print(f"OR: 10 | 3 ={10 | 3}") #1011
print(f"XOR: 10 ^ 3= {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}")
print (f" desplazamiento hacia la derecha: 10 >> 2 = {10 >> 2} ")#0010
print (f" desplazamiento hacia la derecha: 10 << 2 = {10 << 2} ")#101000

#estructuras de control

#condicionales

my_string = "mourodev"
if my_string == "mourodev":
    print ("my_string es mourodev")
elif my_string == "brais":
    print ("my_string es brais")
else:
    print("my_string no es ni mourodev ni brais")

#iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10: 
    print (i)
    i += 1

#manejo de exepciones
try: 
    print(10/0)
except:
    print ("se ha producido un error")
finally:
    print( "ha finalizado el manejo de excepciones")
    
# EXTRA 

for number in range(10 , 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print (number)
    
