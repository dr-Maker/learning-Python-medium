def run():
    my_lista = [1 , "hola", True, 4.5 ]
    my_diccionario = {"primerNombre":"Jonathan", "Apellido":"Venegas"}

    super_lista = [
        {"primerNombre":"Jonathan", "Apellido":"Venegas"},
        {"primerNombre":"Facundo", "Apellido":"Garcia"},
        {"primerNombre":"Miguel", "Apellido":"Rogelio"},
        {"primerNombre":"Pepe", "Apellido":"Perez"},
    ]


    super_diccionario = {
        "numeros_naturales" : [1,2,3,4,5],
        "numeros_enteros": [-2,-1,0,5],
        "numero_decimal": [1.2 , 5.6, 7.9, 9.0]        
    }

    
    for key, value in super_diccionario.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()
