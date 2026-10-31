print("People up to and including 26 years of age are exempt from paying taxes in poland")
print("let's see if ur eligible for that law!")
 
age = input("Type down ur age: ")
if len(age) > 3 and not age.isalpha():
    raise ValueError("please type ur real age")

    


def eligibility_for_taxes(age):
    if int(age) <= 26: 
        print("You don't need to pay taxes, Yay!")
    else: 
        print("You need to pay taxes :(") 
eligibility_for_taxes(age)