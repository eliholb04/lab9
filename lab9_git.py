from encoder import encode


menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit"
n=0

while True:
    print(menu)
    menu_opt = input("Please enter an option: ")
    if menu_opt == 1 or menu_opt == 2 or menu_opt == 3:
        if menu_opt == 1:
            enc_mess = input("Please enter your password to encode: ")
            if encode(enc_mess) is not None:
                encoded = encode(enc_mess)
                print("Your password has been encoded and stored!")
        elif menu_opt == 2:
            print(f"The encoded password is {encoded}, and the original password is ")
        elif menu_opt == 3:
