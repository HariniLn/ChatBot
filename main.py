# Declare the 3 lists
list_happy_words = ["joyful", "happy", "amazing", "beautiful"]
list_sad_words = ["sad", "tears", "crying", "depressed"]
list_games = ["tetris", "flappy bird", "snake"]

def happy_feeling(input, happy_words):
  for i in happy_words:
    if i in input:
      return "happy"
  return "unknown"

def sad_feeling(input, sad_words):
  for i in sad_words:
    if i in input:
      return "sad"
  return "unknown"

# Initialize the games_index variable
games_index = 0
# A variable to tell if the program should break from the while loop
set_break_flag = False

# This while loop goes on infinitely
# Till it encounters a break in the program
while True:
  # ask the user to input a word describing their feeling, save the string
  feeling = input('How are you feeling today?')
  # Check if the word is a part of the happy list
  feeling_lower = feeling.casefold()
  predicted_feeling = happy_feeling(feeling_lower, list_happy_words)
  if predicted_feeling == "happy":
    print("Glad to know!")
    break
  else:
    # Check if games list is over
    # This can be done in several way, we will
    # use the index to determine this
    if games_index >= len(list_games):
      print('Sorry, we are out of games to suggest')
      break
    else:
      predicted_feeling = sad_feeling(feeling_lower, list_sad_words)
      if predicted_feeling == "sad":
        print('Sorry you feel this way.')
        print('Please play ', list_games[games_index])
        games_index = games_index + 1
          # Note that below break is just for the for loop, not the while loop
        # Go back to asking user how they feel
      else:
        print('I dont understand how you feel!')
        break

  