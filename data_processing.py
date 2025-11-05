import csv, os

# woah i might steal i mean borrow this
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def filter_(condition, dict_list):
    filtered = []
    for item in dict_list:
        if condition(item, filtered):
            filtered.append(item)
    return filtered


def aggregate(aggregation_key, aggregation_function, dict_list):
    filtered = filter_(aggregation_function, dict_list)
    return [item[aggregation_key] for item in filtered]


cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities
for city in cities[:5]:
    print(city)
print()


# Print the average temperature of all the cities
print("The average temperature of all the cities:")
condition = lambda city, filtered: True
temps = [float(temp) for temp in aggregate("temperature", condition, cities)]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany:")
condition = lambda city, filtered: city["country"] == "Germany"
germanies = aggregate("city", condition, cities)
print(germanies)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
condition = lambda city, filtered: city["country"] == "Spain" and float(city["temperature"]) > 12
hot_spains = aggregate("city", condition, cities)
print(hot_spains)
print()

# Count the number of unique countries
print("Number of unique countries:")
condition = lambda city, filtered: city["country"] not in [item["country"] for item in filtered]
uniques = aggregate("city", condition, cities)
print(len(uniques))
print()

# Print the average temperature for all the cities in Germany
print("Average temperature for all the cities in Germany:")
condition = lambda city, filtered: city["country"] == "Germany"
germany_temps = [float(temp) for temp in aggregate("temperature", condition, cities)]
print(sum(germany_temps)/len(germany_temps))
print()

# Print the max temperature for all the cities in Italy
print("Max temperature for all the cities in Italy:")
condition = lambda city, filtered: city["country"] == "Italy"
italy_temps = [float(temp) for temp in aggregate("temperature", condition, cities)]
print(max(italy_temps))
print()
