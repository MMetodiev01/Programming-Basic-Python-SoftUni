movie_name = input()
days_count = int(input())
tickets_count = int(input())
tickets_price = float(input())
percent_for_cinema = int(input())

price_ticket_for_day = tickets_price * tickets_count
income_for_period = days_count * price_ticket_for_day
income_for_cinema = income_for_period * percent_for_cinema / 100
total_income_for_movie = income_for_period - income_for_cinema
print(f"The profit from the movie {movie_name} is {total_income_for_movie:.2f} lv.")