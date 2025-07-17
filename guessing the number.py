import random
def match():
    global score
    secret_number = random.randint(1,10)
    i=3
    i_limit = 0
    while i>i_limit:
        print(f">>> You have {i} chance")
        guess = int(input("Guess the number (between 1 to 10): "))
        i -= 1
        #print(i)
        if guess == secret_number:
                print("You got it right !")
                score+=1
                break
    else:
        print("> You lost!")
        #print(f"> The correct number was {secret_number}")

option1=input("Press E to enter Q to quit > ").upper()
if option1 == "E":
    print('''>>> Best of 3 matches. 
>>> You will have a total of 3 chances in each match''')
    main_score=0
    while option1 == "E" or "Y":
        score=0
        for m in range(1,4):
            print(f"Match {m}")
            match()
        if score >=2 :
            print("You won the Game!")
            main_score+=1
        else:
            print("You lost the Game!")
        option1=input("Press Y to play again Q to quit  ").upper()
        if option1=="Q":
            print(f"Games won: {main_score}")
            break
elif option1=="Q":
    print("Thanks for playing")
    exit()
    
