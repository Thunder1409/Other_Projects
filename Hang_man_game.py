def rules():
    print("There is an inocent person")
    print("Which will die if you will guess the wrong word")
    print("Try your best. All the best")

import random
words = ['india']
random = random.choice(words)
allowed_v = set('abcdefghijklmnopqrstuvwxyz')

name = input("Enter your name:")
print("==========")

ru = input("press enter to know the rules")
print("==========")
rules()

l = ["""
           -------   """,
     
     """
           -------
              O      """,
     
     """
           -------
              O
              |      """,
     
     """
           -------
              O
              |
             /       """,

     """
           -------
              O
              |
             / \     """,
     
     
     """
           -------
              O
              |--
             / \     """,
     
     """
           -------
              O
            --|--
             / \     """]



word_cop = "_" * len(random)
print("*", word_cop, "*")
print("")
print("Length of word is: ", len(random))
print("============================")

s = set('abcdefghijklmnopqrstuvwxyz')
tries = 7
count = 0
counter = 0
z = 0

while word_cop != random and count < tries:
    guess = input("Enter your word:\n")
    counter = counter + 1
    print()
    
    if guess in s:
        print()

    else:
        print("Wrong input. Try again")
        counter = counter - 1

    if guess in random:
        for i in range(0, len(random)):
            if guess == random[i]:
                word_cop = word_cop[:i] + guess + word_cop[i+1:]
        print(word_cop)

    else:
        print(l[z])
        count = count + 1
        print()
        print()
        z = z+1
    
if word_cop == random:
    print("You cracked it in", counter, "tries")
    print("The word was", random)

elif count > tries:
    print("You failed and let a person died :(")
    print("The word was", random)

else:
    print("You failed and let a person died :(")
    print("The word was", random)


print("Thanks for playing", name)
