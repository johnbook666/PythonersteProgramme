print('--- secret number ---')
secret = 7
guess = int(input('guess the number (1-10) ? '))
if guess == secret:
    print('congrats !')
else:
    print('wrong number. It is not: ' + str(guess))