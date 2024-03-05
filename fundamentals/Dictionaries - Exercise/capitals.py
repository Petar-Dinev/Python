countries = input().split(', ')
capitals = input().split(', ')
my_dict = dict(zip(countries, capitals))

for country, capital in my_dict.items():
    print(country, '->', capital)
