# Part a 

def calculate_total_sales(game):
    result = game[NA_SALES] + game[EU_SALES] + game[JP_SALES]
    return result
print(calculate_total_sales(video_game_sales[0]))
print()

# Part b

def filter_by_genre(data, genre='Platform'):
    result = []
    for game in data:
        if game[GENRE] == genre:
            result.append(game)
    return result
print(len(filter_by_genre(video_game_sales)))
print()
print(len(filter_by_genre(video_game_sales, 'Action')))
print()

# Part c

def get_summary(game):
        result = (f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}M")
        return result
for row in video_game_sales:
    print(get_summary(row))
