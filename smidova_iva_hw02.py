import json

file_in_lines = []

with open("netflix_titles.tsv", mode="r", encoding="utf-8") as file:
    for line in file:
        split_text = line.split("\t")
        file_in_lines.append(split_text)

headline = file_in_lines[0]
rows = file_in_lines[1:]

index_title = headline.index("PRIMARYTITLE")
index_directors = headline.index("DIRECTOR")
index_cast = headline.index("CAST")
index_genres = headline.index("GENRES")
index_decade = headline.index("STARTYEAR")

movie_info = []

for row in rows:
    movie_values = {}
    # Add tittle
    movie_values["title"] = row[index_title]
    # Add directors
    directors = row[index_directors]
    directors = directors.split(", ")
    if directors == [""]:
        movie_values["directors"] = []
    else:
        movie_values["directors"] = directors
    # Add cast
    cast = row[index_cast]
    cast = cast.split(", ")
    if cast == [""]:
        movie_values["cast"] = []
    else:
        movie_values["cast"] = cast
    # Add genres
    genres = row[index_genres]
    movie_values["genres"] = genres.split(",")
    # Add decade
    decade = row[index_decade]
    decade = int(decade) - int(decade[-1])
    movie_values["decade"] = decade
    # Append movie_values into movie_info
    movie_info.append(movie_values)

with open("hw02_output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(movie_info, output_file, ensure_ascii=False, indent=4)