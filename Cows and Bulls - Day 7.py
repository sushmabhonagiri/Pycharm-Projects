
import random # Always import at top
# set Variables or constants
random_number = random.randint(1000, 9999)
cows = 0
bulls = 4
print(f"DEBUG: {random_number}\n") # This gives you a reminder its a debug tool
# Here your game begins
print(" Welcome to the Cows and Bulls Game ! ")
while True:
    guess = int(input("Guess the number : "))
    if guess < 1000 or guess > 9999: # Changed this, it reads better this way :)
        print("Wrong Format ") # error when wrong entry is made
    elif guess != random_number:
        def split(word):
            return list(word)

        guess_list = (split(str(guess)))
        print(guess_list)
        rand_list = split(str(random_number))
        print(rand_list)

        for p,v in enumerate(rand_list):
            if rand_list[p] == guess_list[p]:
                cows += 1
                bulls = bulls-1
        print(str(cows) + "cows, " + str(bulls) + "bulls")


    elif guess == random_number: # Checks if correct
        break
print("You got it!")

