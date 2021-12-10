from Tittle_Bar import display_title_bar
from ParImpar import number_validation

choice = ''
display_title_bar()
while choice != 'q':    
    
    # Let users know what they can do.
    print("\n[1] Validar si un número es par o impar.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.")
    
    choice = input("What would you like to do? ")
    
    display_title_bar()
    if choice == '1':
        print("\nHere are the people I know.\n")
    elif choice == '2':
        print("\nI can't wait to meet this person!\n")
    elif choice == 'q':
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")