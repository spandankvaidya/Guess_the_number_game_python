import random
print("Welcome to the Game:Guess the number!")
print("You have 10 chances of guessing a random number within the range you specify. ")
print("Score will be generated on how accurately you guess")
print("Remember; the broader the range you set, the higher you score")
print("Remember; more the guesses you take, the lesser you score ")
input("Press enter to continue")
s_r=int(input("Range Start: "))
e_r=int(input("Range end: "))
random_num=random.randint(s_r,e_r)
x=e_r-s_r

n=10

for i in range (n):
    print('Chance number:',i+1)
    g = int(input("Guess the number:"))
    if g!=random_num:
        if g>random_num:
            print("Sorry, wrong guess.Guessed number is higher than correct number")
        elif g<random_num:
            print("Sorry, wrong guess.Guessed number is lower than correct number")
    else:
        print(f'Congratulations, you have guessed the correct number: {random_num} in', i+1," guesses")
        score = x / (i+1)
        print('You have scored:',score," points! ")
        break




