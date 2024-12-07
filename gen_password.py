import random

# Rendiamo la generazione della password un metodo in modo da poter chiamare ed 
# eseguire il metodo in altre parti del codice

def gen_new_password(pass_length): # Come parametro in mezzo alle parentesi mettiamo una variabile
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password