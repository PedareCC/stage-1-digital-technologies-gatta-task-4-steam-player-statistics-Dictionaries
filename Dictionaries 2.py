# Steam wants you to take dictionary of player scores and work out who the top players are and who the worst players are.

# Step 1: Underneath the dictinary on line 16, use a 'for' loop to print all of the player names.

# Dictionary of player scores
player_scores = {
    "Scorpion": 85,
    "Sub-Zero": 90,
    "Raiden": 75,
    "Liu Kang": 92,
    "Sonya": 88,
    "Jax": 70,
    "Kano": 65
}

for 
    print(

# Step 2: On line 21, use a 'for' loop to print all of the player names alongside their scores.

for 
    print(  


# Step 3: A dictionary has been created for 'top players' who have a score above 70. Below, create a dictionary for 'bottom players' who have a score below 70.

top_players = {player: score for player, score in player_scores.items() if score >= 70}
print(top_players)
      



