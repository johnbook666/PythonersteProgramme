print('--- mood checker ---')
print('enter mood: happy, nervous, sad, excited, relaxed')
mood = input('your mood ? ')
if mood == "happy":
    print('It is great to see you happy!')
elif mood == "nervous":
    print('Take a deep breath 3 times.')
elif mood == "sad":
    print('take a walk and enjoy the sun !')
elif mood == "excited":
    print('get the party started !')
elif mood == "relaxed":
    print('feel free to relax more')
else:
    print('I don't recognize this mood. Next time :-)')
