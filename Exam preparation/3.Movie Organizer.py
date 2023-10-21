from collections import defaultdict


def movie_organizer(*args):
    movies = defaultdict(list)  # Може и setdefault(genre, []).append()
    for name, genre in args:
        movies[genre].append(name)
    movies = dict(sorted(movies.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = ""
    for genre, names in movies.items():
        result += f"{genre} - {len(names)}\n"
        for name in sorted(names):
            result += f"* {name}\n"
    return result


print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print()
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print()
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

