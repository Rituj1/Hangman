import random
print('Welcome to the Hangman Game!')
print("You have six lives to guess and win the game and if you aren't able to do so you will be hanged to death!")



word = ['apple', 'banana', 'cherry', 'dragonfruit', 'strawberry']
chosen_word = random.choice(word)
print("You have to name the correct fruit using the hints before you run out of lives!\n")
if chosen_word == 'apple':
    print("Hint: Favourite Fruit of Physics!")
elif chosen_word == 'banana':
    print("Hint: It's chips are awesome!")
elif chosen_word == 'cherry':
    print("Hint: You can eat it but cherish it first!")
elif chosen_word == 'dragonfruit':
    print("Hint: The Fruit of Dragons!")
elif chosen_word == 'strawberry':
    print("Hint: You can eat it but you can't straw it!")


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



display = []
for _ in range(len(chosen_word)):
    display += '_'
print(display)
lives = 6
game_ends = False
while not game_ends:
    user_entry = input('Guess a letter: ').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_entry:
            display[position] = letter

    print(f"{' '.join(display)}")


    if user_entry not in chosen_word:
        lives -= 1
        if lives == 0:
            game_ends = True
            print('You Lost!\nGame Over!')

    if '_' not in display:
        game_ends = True
        print('You Win!')

    print(stages[lives])

