# hangman8_8.py
import random

print("H A N G M A N")
print()

words = ['python', 'java', 'kotlin', 'javascript']
play_or_exit = None

while play_or_exit != "play" and play_or_exit != "exit":
    play_or_exit = input('Type "play" to play the game, "exit" to quit: ')
    if play_or_exit == "play":
        # set initial conditions for a new game
        lives = 8
        position = 0
        word = random.choice(words)
        visible_word = ("-" * len(word))
        letters_left = set(word)
        letters_guessed = set()
        game_status = None
        print()
    elif play_or_exit == "exit":
        lives = 0  # ensures the program skips the while loop below
        game_status = "EXIT"
    else:
        continue


    while lives != 0:
        print(visible_word)
        letter = input("Input a letter: ")

        if len(letter) != 1:  # user enters more or less than 1 character
            print("You should input a single letter")
        elif letter in letters_guessed:  # user already guessed this letter
            print("You've already guessed this letter")
        elif not letter.islower():  # letter is a capital or non ASCII character
            print("Please enter a lowercase English letter")
        elif letter in word:
            letters_guessed.add(letter)  # add the guessed letter to this set
            letters_left.discard(letter)  # remove the guessed letter from the set
            frequency = word.count(letter)  # frequency of letter in word

            for _ in range(frequency):
                i = word.find(letter, position)  # index letter
                visible_word = visible_word[:i] + letter + visible_word[i+1:]
                position = i + 1  # next iteration start searching  from this position
            
            if letters_left == set():
                game_status = "WON"
                print()
                print(visible_word)
                break

            position = 0  # reset to 0 after a letter has been found  
        else:
            print("That letter doesn't appear in the word")
            letters_guessed.add(letter)
            lives -= 1

        if lives != 0 and game_status != "WON":  # winning condition
            print()  # just for layout


    if game_status == "WON":
        play_or_exit = None
        print("You guessed the word!")
        print("You survived!")
    elif game_status == "EXIT":
        pass
    else:
        play_or_exit = None
        print("You lost!")