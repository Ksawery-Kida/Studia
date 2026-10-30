def number_of_letters(name, surname):   
    characters_in_name = len(name)
    characters_in_surname = len(surname)
    print(f'Your name has {characters_in_name} characters')
    print(f'Your surname has {len(surname)} characters')
    print(f'Your full name has {characters_in_name + characters_in_surname} characters overall')
number_of_letters(name = "ksawery", surname = "kida" )
