# Part a

game_name = video_game_sales[4][NAME]
print(game_name[:7])

# Part b
 
for name in messy_names:
    name = name.strip().lower()
    print(name)

# Part c 

game = video_game_sales[0]
print(f"#1 Best Seller: {game[NAME]} ({game[YEAR]}) - ${game[GLOBAL_SALES]}M global sales")
