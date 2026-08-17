# Part a 

sales_by_genre = {}
for row in video_game_sales:
    key = row[GENRE]
    value = row[GLOBAL_SALES]
    if key in sales_by_genre:
        sales_by_genre[key] = sales_by_genre[key] + value
    else:
        sales_by_genre[key] = value
print(sales_by_genre)
print()

# Part b 

games_per_publisher = {}
for row in video_game_sales:
    key = row[PUBLISHER]
    if key in games_per_publisher:
        games_per_publisher[key] = games_per_publisher[key] + 1
    else:
        games_per_publisher[key] = 1
print(games_per_publisher)
print()

# Part c

top_game = {'name' : video_game_sales[0][NAME], 'year' : video_game_sales[0][YEAR], 'genre' : video_game_sales[0][GENRE], 'publisher' : video_game_sales[0][PUBLISHER], 'global_sales' : video_game_sales[0][GLOBAL_SALES]}
for key, value in top_game.items():
    print(f"{key} : {value}")
