import sys

films_count = int(input())
top_movie_rating = -sys.maxsize
low_movie_rating = sys.maxsize
best_rating = ""
low_rating = ""
total_rating = 0
for i in range(1, films_count + 1):
    movie_name = input()
    rating_film = float(input())
    total_rating += rating_film

    if rating_film >= top_movie_rating:
        top_movie_rating = rating_film
        best_rating = movie_name
    if rating_film <= low_movie_rating:
        low_movie_rating = rating_film
        low_rating = movie_name

average_raring = total_rating / films_count
print(f"{best_rating} is with highest rating: {top_movie_rating:.1f}")
print(f"{low_rating} is with lowest rating: {low_movie_rating:.1f}")
print(f"Average rating: {average_raring:.1f}")