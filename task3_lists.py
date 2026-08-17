# Part a 

game_names = []
for row in video_game_sales:
    game_names.append(row[NAME])
print(game_names)

# Part b

new_game = [21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18]
video_game_sales.append(new_game)
print(len(video_game_sales))

# Part c

number_of_columns = len(video_game_sales[0])
number_of_games = len(video_game_sales)
dataset_info = (number_of_games, number_of_columns, 'Video Game Sales')
print(dataset_info)
# Using a tuple instead of a list to store the metadata, "dataset_info", protects the elements inside the tuple from being removed or modified by later code lines.
