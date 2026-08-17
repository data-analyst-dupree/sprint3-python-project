# Part a 

for row in video_game_sales:
    if row[GLOBAL_SALES] > 25:
        print(row[NAME], row[GLOBAL_SALES])

# Part b

pre_2000_count = 0
for row in video_game_sales:
    if row[YEAR] < 2000:
        pre_2000_count = pre_2000_count + 1
print(pre_2000_count)

# Part c

na_sales = 0
jp_sales = 0
for row in video_game_sales:
    na_sales = na_sales + row[NA_SALES]
    jp_sales = jp_sales + row[JP_SALES]
if na_sales > jp_sales:
    print(f"North America had the higher sales. North America sales: ${na_sales:.2f}M, Japan sales: ${jp_sales:.2f}M.")
elif na_sales == jp_sales:
    print(f"Both Japan and North America had equal sales at ${na_sales:.2f}M.")
else:
    print(f"Japan had the higher sales. Japan sales: ${jp_sales:.2f}M, North America Sales: ${na_sales:.2f}M.")

# Part d 

nintendo_games = []
for row in video_game_sales:
    if row[PUBLISHER] == 'Nintendo':
        nintendo_games.append(row[NAME])
print(nintendo_games)
print(len(nintendo_games))
