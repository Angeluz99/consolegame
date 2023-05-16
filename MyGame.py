# Juego de matemáticas y ortograía.



from random import * #import random #as rd #from random import randint 
n = randint(1,6)  
nr = randint(1,6)       #random.randint() # rd.randint() #randint() #

instructions= " 'x' para finalizar el juego.  \n 'i' para iniciar. \n"
rules= "\n -Primero apuesta para acumular billetes, luego responde. \n -Si te quedas sin billetes pierdes.\n Inicias con 6 billetes [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]  [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]  [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]  [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]  [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]  [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] "
error= "Tecla no reconocida"
bet= "¿CÚANTO APUESTAS?:"
errorbet = "Eso es más de lo que tienes. (ಠ_ಠ)┌∩┐"
points= 6
stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]" * points
nopoints= "Te has quedado sin puntos para apostar. (⋟﹏⋞) "


a_two = int((6 - n) + (3 * (nr / 1)))
q_two= f"(6 - {n}) + (3 * ({nr} / 1))= ¿? \n ¿Cuál es el total? \n"

q_three= " se lee igual tanto de derecha a izquierda, como de izquierda a derecha.\n Cierto: presiona 'c' \n Falso: presiona 'f' "


def endgame():
    print("Gracias por jugar")
    exit()

def q_six():
    counter_six=0
    while counter_six < 4:
        n=randint(1,9)
        nr=randint(1,9)
        print(f"{nr} y {n} = {abs(nr - n)}{nr + n}")
        counter_six += 1


def game():

    def qsix(points, stars):
        print(f"{n} y {nr} = ¿?")
        a_six=(f"{abs(nr - n)}{nr + n}")
        #print(a_six)
        print (f"\n Tienes {points} {stars}")
        if points <= 0:
            print (f"{nopoints}\n ¡Vuelve a Intentarlo!\n\n Jugar de nuevo 'i'. \n Salir del juego 'x'")
            if input() =='i':
                game()
            else:
                print("Has salido del juego. (╯°□°）╯ \n\n")
                endgame()
        print(bet)
        bet6 = int(input())       
        while True:
            if bet6 > points:
                print(f"{errorbet} \n Tienes {points} {stars} {bet}")               
                bet6 = int(input())
            else:
                break
          
        print ("\nTu respuesta es: ")
        player_ans6= int(input())
        if player_ans6 == int(a_six):
            points = points + bet6
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print ("¡Correcto! ٩(^‿^)۶\n \nFin del juego")
            print (f"Terminaste con {points} billetes. {stars}\n")
            faces(points)
           
        else:
            points = points - bet6
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print("Fallaste.(-_- ;)\n  \nFin del juego")
            print (f"Terminaste con {points} billetes. {stars}\n")
            faces(points)

    def qfive(points, stars):
        dic_five = {"'Si la soprano vuelve en si, si podriamos tocar la pieza en si menor.'": 3 , "'Te puedo preparar un te cuando tu me lleves a tu casa'": 2, "'No se por que el aun espera que le de mi amistad'":4 , "'Mi tia no recuerda la ultima vez que bebimos'": 2 }
        q_five= choice(list(dic_five))
        print(f"\n Quinta pregunta: \n {q_five} \n ¿Cuántos acentos le faltan a la oración: '2', '3', o '4'?:\n Tienes {points} {stars}")
        #a_five= int(input())
        if points <= 0:
            print (f"{nopoints} \n ¡Vuelve a Intentarlo!\n\n Jugar de nuevo 'i'. \n Salir del juego 'x'")
            if input() =='i':
                game()
            else:
                print("Has salido del juego. (╯°□°）╯ \n\n")
                endgame()
        print(bet)
        bet5 = int(input())
        while True:
            if bet5 > points:
                print(f"{errorbet} \n Tienes {points} {stars} {bet}")
                bet5 = int(input())
            else:
                break
        print ("\nTu respuesta es: ")
        player_ans5= int(input())
        if player_ans5 == dic_five[q_five]:
            points = points + bet5
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print ("¡Correcto!٩(^‿^)۶\n \n Última pregunta: ")
            q_six()
            #print (f"\n Tienes {points} {stars}")
            qsix(points, stars)
        else:
            points = points - bet5
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print("Fallaste. (-_- ;)\n\n Última pregunta: \n")
            q_six()
            #print (f"\n Tienes {points} {stars}")
            qsix(points, stars)
        

    def qfour(points, stars):
        l_four = ['x','y','z','k']
        shuffle(l_four)
        r_four = ''.join(l_four)
        q_four= (f" {l_four[1]} > {l_four[0]} . {l_four[1]} < {l_four[2]} . {l_four[3]} > {l_four[0]} . {l_four[3]} > {l_four[2]}: \nCrea una lista de menor a mayor con las cuatro letras. \nEjemplo: kxyz (> mayor que >, < menor que <).\n ")
        print(f"{q_four}\n Tienes {points} {stars}")
        if points <= 0:
            print (f"{nopoints} \n ¡Vuelve a Intentarlo!\n\n Jugar de nuevo 'i'. \n Salir del juego 'x'")
            if input() =='i':
                game()
            else:
                print("Has salido del juego. (╯°□°）╯ \n\n")
                endgame()
        #print(r_four)
        print(bet)
        bet4 = int(input())
        while True:
            if bet4 > points:
                print(f"{errorbet} \n Tienes {points} {stars}{bet}")     
                bet4 = int(input())   
            else:
                break
        print ("\nTu respuesta es: ")
        player_ans4= input()
        if player_ans4 == r_four:
            points = points + bet4
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print (f"¡Correcto!٩(^‿^)۶\n")
            qfive(points, stars)
        else:
            points = points - bet4
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print(f"Fallaste. (-_- ;)\n")    
            qfive(points, stars)
         

    def qtrhee(points, stars):
        
        l_three = ["'Roma ni se conoce sin odio, ni se conoce sin amor.'","'No son robos, solo son sobornos.'","'Os sacáis la ropa, por si acaso.'","'Allí toca Pedro Netoxas, saxo-tenor de pacotilla.'","'La ruta nos aportó otro paso natural.'"]
        s_three = choice(l_three)
        l_falso =["'Roma ni se conoce sin odio, ni se conoce sin amor.'","'No son robos, solo son sobornos.'","'Os sacáis la ropa, por si acaso.'"]
        l_cierto = ["'Allí toca Pedro Netoxas, saxo-tenor de pacotilla.'","'La ruta nos aportó otro paso natural.'"]

        print (f"{s_three}{q_three}\n Tienes {points} {stars}")
        if s_three in l_falso:
            a_three ="f"

        elif s_three in l_cierto:    
            a_three ="c"
        if points <= 0:
            print (f"{nopoints} \n ¡Vuelve a Intentarlo!\n\n Jugar de nuevo 'i'. \n Salir del juego 'x'")
            if input() =='i':
                game()
            else:
                print("Has salido del juego. (╯°□°）╯ \n\n")
                endgame()
        print(bet)
        bet3 = int(input())
        while True:
            if bet3 > points:
                print(f"{errorbet} \n Tienes {points} {stars}{bet}")
                bet3 = int(input())      

            else:
                break
        print ("\nTu respuesta es: ")
        player_ans3 = input()
        if player_ans3 == a_three:
            points = points + bet3
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print (f"\n ¡Correcto!٩(^‿^)۶\n \nCuarta pregunta: ")
            qfour(points, stars)
        else:
            points = points - bet3
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print (f"Fallaste.(-_- ;)\n  \nCuarta pregunta: ")
            qfour(points, stars)
        


    def qtwo(points, stars):
        if points <= 0:
            print (f"{nopoints}\n ¡Vuelve a Intentarlo!\n\n Jugar de nuevo 'i'. \n Salir del juego 'x'")
            if input() =='i':
                game()
            else:
                print("Has salido del juego. (╯°□°）╯ \n\n")
                endgame()
        print(bet)
        bet2 = int(input())
        while True:
            if bet2 > points:
                print(f"{errorbet} \n Tienes {points} {stars}{bet}")
                bet2 = int(input())
            else:
                break
        #print(a_two)
        print ("\nTu respuesta es: ")
        player_ans2= int(input())
        if player_ans2== a_two:
            points = points + bet2
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print (f"\n ¡Correcto! ٩(^‿^)۶\n \nTercer pregunta: ")
            qtrhee(points, stars)
        else:
            points = points - bet2
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points 
            print (f"\nFallaste. (-_- ;)\n \nTercer pregunta:")
            qtrhee(points, stars)
        
        

    def qone(points, stars):
        list_one = ("'Aereo y Area'", "'Torax y Arbol'", "'Dialogo y Atentado'" , "'Facil y Albacea'")
        choice_one= choice(list_one)
        list_c =["'Aereo y Area'", "'Torax y Arbol'"]
        list_f = ["'Dialogo y Atentado'" , "'Facil y Albacea'"]
        q_one= f"\n {choice_one} llevan ambas acento. \n Cierto: presiona 'c' \n Falso: presiona 'f'"
        if choice_one in list_c:
            a_one= 'c'
        elif choice_one in list_f:
            a_one = 'f'
        print (f"\nPrimer pregunta: {q_one}")
        print(bet)
        bet1 = int(input())
        while True:
            if bet1 > points:
               print(f"{errorbet} \n Tienes {points} {stars} {bet}")
               bet1 = int(input())
            else:
                break
        print ("\nTu respuesta es: ")
        #print(a_one)
        player_ans1 = input()
        if player_ans1 == a_one:
            points = points + bet1
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print (f"\n ¡Correcto! ٩(^‿^)۶\n \nSegunda pregunta: {q_two}\n Tienes {points} {stars}")
            qtwo(points, stars)
        else:
            points = points - bet1
            stars = " [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] " * points
            print (f"\nFallaste.(-_- ;) \n \nSegunda pregunta:{q_two} \n Tienes {points} {stars}")
            qtwo(points, stars)

       
    def faces(points):
        if points <= 6:
            print("No eres el mejor apostando... o pensando.(-(-_(-_-)_-)-)")
        elif points <= 10:
            print ("Apenitas sacaste pa' las cocas '⌐(ಠ۾ಠ)¬'")
        elif points <= 20:
            print("Bien hecho. Conoces tus limitaciones. (◔/‿\◔) ۜ")
        elif points <= 30:
            print("¡Eres bueno entre los buenos!٩(- ̮̮̃-̃)۶")
        else:
            print("¡Wow! Jugaste excelente. \(סּںסּَ` )/ۜ")

        print("\n\n Presiona 'i' para volver a el menú principal.")
        if input() =='i':
            game()
        else:
            print("Has salido del juego. (╯°□°）╯ \n\n")
            endgame()
            

    print("\n(✿ ♥‿♥) Bienvenido al Juego de Matemáticas y Ortografía.\n__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡._____̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|")
    print(rules)
    print(instructions)
    player_menu= input()
    def endgame():
        print("Gracias por jugar")
        exit()
    if player_menu == "i":
        qone(points, stars)
    elif player_menu == "x":
        print("Has salido del juego. (╯°□°）╯ \n\n")
        endgame()


game()


    


        

