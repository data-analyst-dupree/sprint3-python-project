# Part a

total_games = len(video_game_sales)
print(f"There is a total of {total_games} games.")

# Part b

total_global_sales = 0
for sale in video_game_sales:
    total_global_sales = total_global_sales + sale[GLOBAL_SALES]

avg_global_sales = total_global_sales / total_games
print(f"The average of global sales across all games is ${avg_global_sales:.2f} million dollars.")

# Part c

top_game_share = (video_game_sales[0][GLOBAL_SALES] / total_global_sales) *100
print(f"Wii Sports accounts for {top_game_share:.2f}% of the total global sales.")
