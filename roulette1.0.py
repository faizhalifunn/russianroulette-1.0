import random

def main():
    random_number = random.randint(1, 6)
    # tembak = input("how many shot ?")
    # tembak = int(tembak) 
    hit = 0

    print ("\n\nyou sitting in the middle of the room with a revolver in your hand.... \nyou point your revolver into your mouth... \ntry to gamble on your life..")
    print ("\n------------------------------------------------------------------------------------")
    print ("                         press enter to pull the trigger... \n\n                                        or      \n\n                         type 'run' to continue your life...")
    print ("------------------------------------------------------------------------------------")

    while True:
        user_input = input()  # Wait for the user to press Enter
        if user_input == "run":  # Exit condition
            slisih = random_number - hit
            print("just ", slisih," bullet away...")
            break
        else:
            hit += 1  # Increment the hit counter
            if hit != random_number :
                print ("cklk...")
            else : print("BOOM!... a bullet just penetrate through your head... \n\nit shattered all over the floor");break
    print ("-----------------------------------  game over  -------------------------------------")

while True:
    main() 
    restart_input = input("Press 'Enter' to restart, or type 'exit' to quit")
    if restart_input == "exit":
        print("Goodbye!")