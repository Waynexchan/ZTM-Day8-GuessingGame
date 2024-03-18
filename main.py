import sys
from random import randint

first = int(sys.argv[1])
last = int(sys.argv[2])

def get_user_input(guess):
    while True:
        try:
            guess_no = int(input(guess))
            if int(sys.argv[1]) < guess_no < int(sys.argv[2]): #用sys.argv 黎讀取command入既值
                return guess_no
            else:
                print(f'Bro, you have to enter the correct number between {first} and {last}')

        except ValueError as err:
            print(f"Please enter integers Error: {err}")


correct_number = randint(int(sys.argv[1]),int(sys.argv[2])) #用RANDINT去讀取RANDOM NO
print(correct_number) #Testing

guess = f'Please enter a number between{first} and {last}: '
guess_number = get_user_input(guess)

while True:
    if guess_number > correct_number:
        last = guess_number-1
    elif guess_number < correct_number:
        first = guess_number+1
    else:
        print(f'You are Genius. The correct number is {correct_number}')
        break

    guess = f'Please enter a number between{first} and {last}: '
    guess_number = get_user_input(guess)


