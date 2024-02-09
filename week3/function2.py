def imdb_above_55(movie):
    return movie["imdb"] > 5.5

def movies_above_55(movies):
    return [movie for movie in movies if imdb_above_55(movie)]

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def average_imdb(movies):
    total_imdb = sum(movie["imdb"] for movie in movies)
    return total_imdb / len(movies) if len(movies) > 0 else 0

def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)

movies = [ { "name": "Usual Suspects", "imdb": 7.0, "category": "Thriller" }, { "name": "Hitman", "imdb": 6.3, "category": "Action" }]

print(imdb_above_55(movies[0])) 
print(movies_above_55(movies)) 
print(movies_by_category(movies, "Romance")) 
print(average_imdb(movies)) 
print(average_imdb_by_category(movies, "Romance")) 