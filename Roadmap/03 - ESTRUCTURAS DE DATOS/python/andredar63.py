 #listas
 
my_list = ["andres","black","wolfy"]
print(my_list)
my_list.append("castor")#insercion
print(my_list)
my_list.remove("andres")
print(my_list)
print(my_list[1])
my_list[1]= "cuervillo"
print(my_list)
my_list.sort()#ordenacion
print(my_list)

#tuplas

my_tuple = ("andres","rojas", "andrear63")
print(my_tuple[1])
print(my_tuple)
my_tuple =tuple( sorted(my_tuple))
print(type(my_tuple))

#set

my_set ={"andres","rojas", "andrear63"}
print(my_set)
my_set.add ("aerojasg@gmail.com")
print(my_set)
my_set.remove("andres")
sorted(my_set)

#diccionario
my_dict: dict = {"name":"andres",
                 "surname":"rojas",
                 "alias":"andredar63"      
}
my_dict["addres"] = "aerojasg@gmail.com"
del my_dict["surname"]
print(my_dict["name"]) #acceso
print(my_dict)

# extra 

def my_agenda():
    
    agenda = {}
  
    
    while True:
    
        print("1.buscar contacto")
        print("2. insertar contacto")
        print("3. actualizar contacto")
        print("4. eliminar contacto")
        print("5. salir")
    
        option  = input("\nseleccione una opción: ")
    #match es un swith que funciona como if elif y else usado para casos que no son complejos
        match option:
            case "1":
                name = input("introduce el nombre del contacto : ")
                if name in agenda :
                    print(f"el número de telefono de {name} es {agenda[name]}.")
                else:
                    print(f"el contacto {name} no existe.")
                pass
            case "2":
                name = input("introducir el nombre del contacto: ")
                phone = input("introducir el teléfono del contacto: ")
                if phone.isdigit() and len(phone) > 0 and len(phone) <=11:
                    agenda[name] = phone 
                     
                else:
                    print("por favor introduce un numero de teléfono valido")
                    pass
            case "3":
                name = input("introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    phone = input("introducir el nuevo teléfono del contacto: ")
                    if phone.isdigit() and len(phone) > len(len) <= 11:
                         agenda[name] = phone 
                    else:
                        print("por favor introduce un numero de teléfono valido")          
                else:
                    print(f"el contacto {name} no existe.")

                pass
            case "4":
                name = input (" Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"el contacto {name} no existe.")
                pass
            case "5":
                print("saliendo  de la agenda")
                break
            case _:
                print("opción no valída.elige una opción del 1 al 5.")
my_agenda()
