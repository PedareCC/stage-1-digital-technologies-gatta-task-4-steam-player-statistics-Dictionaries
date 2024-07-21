# A player deletes their account, so you must delete their data from the dictionary.

# Step 1: Below Kano and their score has been removed from the dictionary player_scores. On line 23, also remove Scorpion from the dictionary as well.


player_scores = {
    "Scorpion": 85,
    "Sub-Zero": 90,
    "Raiden": 75,
    "Liu Kang": 92,
    "Sonya": 88,
    "Jax": 70,
    "Kano": 65
}

player_to_remove = "Kano"
if player_to_remove in player_scores:
    del player_scores[player_to_remove]
    print(f"\n{player_to_remove} has been removed.")
else:
    print(f"\n{player_to_remove} not found in the dictionary.")



# Step 2: Print the updated players and scoresw in the dictionary.
