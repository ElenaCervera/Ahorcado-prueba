import sys #estamos llamando al sistema, para que no se cuelgue a la hra de llamar al entorno


MIN=0
MAX=100 #esto hay que cambiarlo segun lo que pidan para los datos. El 100 es pequeño 


def solicitar_introducir_numero(invite): #invite es como un str, se va a comer todo lo que hay ahi. todo lo que etemos ahi va a ser una cadena 
    """
    Esta función verifica que tenemos un número
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end=": ") #invite se rellena a futuro
        datoIntroducido = input()

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            print("Solo están autorizados los caracteres [0-9].", file=sys.stderr)#hay que modificarlo porque el file lee los numeros que hay en esta fila
        else:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido

def solicitar_introducir_numero_extremo(invite, minimum=MIN, maximum=MAX):
    """
    Esta función utiliza el anterior y añade una post-condición
    sobre los extremos del número a introducir
    """
    invite = "{} entre {} y {} incluídos".format(invite, minimum, maximum)
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        datoIntroducido = solicitar_introducir_numero(invite)

        if minimum <= datoIntroducido <= maximum:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido