#Name: Helber diaz vasquez
#Class: 5th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
def run_rating_prototype():
  print("=== Runway Rating System Prototype ===")

  # 1. Get the number of players
  while True:
    try:
      num_players = int(input("Enter the number of players voting: "))
      if num_players > 0:
        break
      print("Please enter at least 1 player.")
    except ValueError:
      print("Invalid input. Please enter a whole number.")

  ratings = []
  print("\n--- Voting Round Started (Rate from 1 to 5) ---")

  # 2. Collect ratings from each player
  for player in range(1, num_players + 1):
    while True:
      try:
        score = float(input(f"Player {player}, enter your rating (1-5): "))
        if 1 <= score <= 5:
          ratings.append(score)
          break
        print("Rating must be between 1 and 5.")
      except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")

  # 3. Calculate and display the average score
  average_score = sum(ratings) / len(ratings)

  print("\n=== Runway Results ===")
  print(f"Total Votes: {num_players}")
  print(f"Average Score: {average_score:.2f} / 5.00")


if __name__ == "__main__":
  run_rating_prototype()