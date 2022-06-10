
def game_instruction():
    print( """Wordle is a single player game
        A player has to guess a five letter hidden word
        You have six attempts
        Your Progress Guide "✔❌❌✔➕"
        "✔" Indicates that the letter at that position was guessed correctly
        "➕" indicates that the letter at that position is in the hidden word, but in a different position
        "❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """ )

def check_word():
    hidden_word = "snail"
    attempt = 6
    while attempt > 0:
        guess = str(input('Guess the word: '))
        if guess == hidden_word:
            print('You guessed the words correctly! WIN')
            break
        else:
            attempt -= 1
            print(f"you have {attempt} attempt(s) ,, \n")


game_instruction()