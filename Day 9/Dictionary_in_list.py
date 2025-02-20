country = input()
visits = int(input())
list_of_cities = eval(input())

travel_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    }
]
print(travel_log)
def add_new_country(country, visits, list_of_cities):
    travel_log.append({
        "country" : country,
        "visits" : visits,
        "cities" : list_of_cities
    })
    

add_new_country(country, visits, list_of_cities)
print(travel_log)