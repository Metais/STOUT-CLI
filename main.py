from STOUT import translate_forward, translate_reverse


infinite_loop = True

while infinite_loop:
    print("Welcome to the SMILES to IUPAC name translator!")
    print("Please enter the number of the option you would like to select:")
    print("1. SMILES to IUPAC name")
    print("2. IUPAC name to SMILES")
    print("3. Exit")
    user_input = input()
    if user_input == '1':
        print("Please enter the SMILES string you would like to convert (or 'back' if you want to go back):")
        SMILES = input()
        if SMILES == 'back':
            continue
        if SMILES[0] == "'" and SMILES[-1] == "'":
            SMILES = SMILES[1:-1]
        IUPAC_name = translate_forward(SMILES)
        print("IUPAC name is: " + IUPAC_name)
    elif user_input == '2':
        print("Please enter the IUPAC name you would like to convert (or 'back' if you want to go back):")
        IUPAC_name = input()
        if IUPAC_name == 'back':
            continue
        SMILES = translate_reverse(IUPAC_name)
        print("SMILES is: " + SMILES)
    elif user_input == '3':
        infinite_loop = False
    else:
        print("Input not recognized. Please try again.")

