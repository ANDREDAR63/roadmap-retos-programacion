"""
funciones definidas por el usuario
"""

# Simple

def greet():
    print ("hola python")

greet()

# con retorno

def return_greet ():
    return ("hola python")

greet = return_greet ()
print (greet)

# con un argumento

def arg_greet ( greet ,name ):
    print (f"{ greet} ,{name}!")

arg_greet("hi","fernanda")# dentro del parentesis va el argumento

# con un argumento predeterminado

def default_arg_greet ( name = "amig@"):
    print (f"hola {name}!")

default_arg_greet()
default_arg_greet()

# con un argumento y retorno

def return_arg_greet ( greet ,name ):
    return f"{ greet} ,{name}!"

print (return_arg_greet("hi","fernanda"))

# con retorno de varios valores

def multiple_return_greet():
    return "hi","fernanda"
greet, name =multiple_return_greet()
print ( greet)
print ( name)

# con una numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f" hola , {name}!")
variable_arg_greet( "python" , "Fernanda" , " andres")

# con una numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key,value in names.items():
        print(f" hola , {value}({key})!")

variable_key_arg_greet(
    language= "python" , 
    name="Fernanda" ,
    edad = 20)

#funciones dentro de funciones

def outer_fuction ():
    def inner_fuction():
        print("funcion interna  :hola python")
        
outer_fuction()

#funciones del lenguaje (buil-in)

print (len("andres"))
print(type(36))
print ("murodev".upper())

#variables locales y globales

global_variable = "phyton"
print(global_variable)

def hello_phyton():
    local_var = "hola"
    print(f"{local_var}, {global_variable}")
hello_phyton()

#EXTRA

def print_numbers(text_1, text_2)-> int:
    count = 0
    for number  in range(1,101):
        if  number % 3== 0 and number  % 5 == 0:
            print(text_1 + text_2)
        elif  number % 5 ==0:
            print(text_2)
        elif number % 3 ==0:
            print(text_1) 
        else:         
            print( number)
            count += 1
    return count

print(print_numbers("fizz","buzz"))
