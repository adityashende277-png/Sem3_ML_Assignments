movies = [
    {"title": "Movie A", "rating": 8.2, "genre": "Thriller"},
    {"title": "Movie B", "rating": 8.4, "genre": "Sports"},
    {"title": "Movie C", "rating": 8.1, "genre": "Comedy"},
    {"title": "Movie D", "rating": 8.2, "genre": "Drama"}
]

# (a) Movies with rating > 8.1
print("Movies with rating > 8.1:")

for movie in movies:
    if movie["rating"] > 8.1:
        print(movie["title"])


# (b) Genres without duplicates
genres = []

for movie in movies:
    if movie["genre"] not in genres:
        genres.append(movie["genre"])

print("\nGenres:", genres)


# (c) Group movies by rating
grouped = {}

for movie in movies:
    rating = movie["rating"]
    title = movie["title"]

    if rating in grouped:
        grouped[rating].append(title)
    else:
        grouped[rating] = [title]

print("\nMovies grouped by rating:")

for rating, titles in grouped.items():
    print(f"Rating {rating}: {', '.join(titles)}")