print("Hi, I'm Monica. Let's get acquainted?")

result_meet = input('Yes or No: ')
while result_meet.lower() != 'yes':
    print('Nothing is clear what are you muttering there')
    result_meet = input('Yes or No: ')
print("I'm glad! It's incredibly boring here")

age = int(input('Are you already an adult? How old are you: '))
while age < 18:
    print('Why then did you climb here? Get out!')
    age = int(input('Are you already an adult? How old are you:'))

print("Let's continue our acquaintance! I'm Monica, I'm 22 years old")
print("Smart guys are my weakness! Let's play a game?")

answer_game = input('Yes or No: ')
while answer_game.lower() != 'yes':
    print('Do not be scared, try it!')
    answer_game = input('Yes or No: ')
print("Great, let's get started!")

town = input('Capital of Canada?: ')
while town != 'Ottawa' and town != 'ottawa' and town != 'OTTAWA':
    print('Your knowledge saddens me. Try again')
    town = input('Capital of Canada?: ')
print('Great. I have superpower. My head is a calculator! Check it!')

what = input('add or subtract? (+ or -): ')
while what != '+' and what != '-':
    print('Dear, choose an option')
    what = input('add or subtract?? (+ or -): ')
a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
if what == '+':
    c = a + b
    print(str(c) + ' - Lol it was easy baby')
elif what == '-':
    c = a - b
    print(str(c) + ' - Lol it was easy baby')

print("Let's play!")
import random

words_bank = [
   'secret', 'world', 'forest',
   'table', 'library', 'informatics',
   'olympiad', 'snowboard', 'christmas'
]

secret_word = random.choice(words_bank)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
   letter = input('Еnter ONE English letter: ').lower()
   if len(letter) != 1:
       continue

   if letter in secret_word:  # hit
       for idx, symbol in enumerate(secret_word):
           if symbol == letter:
               gamer_word[idx] = letter
       if '*' not in gamer_word:  # O(n)
           print('You are winner!')
           break
   else:  # miss
       # errors_counter = errors_counter + 1
       errors_counter += 1
       print('mistakes were made', errors_counter)
       if errors_counter == 8:
           print('You are loser!')
           break

   print(''.join(gamer_word))

#and so on ad infinitum
