#se importa random para generar numeros aleatorios y lo llamamos rd
import random as rd

#se crean las variables billetera y gano 
billetera = 10
gano = 0 
continuar = "si"

print ("Bienvenido a las apuestas")
print("Usted tiene ${} en la billetera".format(billetera))

#se utiliza un ciclo while que cumpla con dos funciones que la billetera sea mayor a cero y que el jugador haya seleecionado que si quiere continuar
while billetera > 0 and continuar =="si":
#dentro del while se agregaron dos condicionales que ayudan a mantener la logica de la apuesta
    apuesta =int(input("Ingrese su apuesta: "))
    if apuesta <= billetera:
        dado1= rd.randint(1,6)
        dado2= rd.randint(1,6)
        total1= dado1 + dado2
        resto = total1%2
        parimpar = input ("Adivina es ¿par o impar?: ")
        print ("sali: {} + {} = {}".format(dado1,dado2,total1))

        if resto == 0 and parimpar =="par":

            print("Gano esta ronda")

            billetera+-apuesta

            gano += 1
        elif resto != 0 and parimpar == "impar":

            print("Gano esta ronda")

            billetera+=apuesta

            gano += 1

        else: 
            print("Perdio esta ronda")

            billetera -= apuesta

        print("Billetera: {}".format(billetera))

        if billetera != 0:

            continuar = input ("Deseas seguir jugando?") #si o no

            (print("-------------------------"))

    

    else:
        print("La apuesta es mayor al dinero que tienes en la billetera")

print("Ganaste {} partidas". format(gano))
print("Gracias por jugar")