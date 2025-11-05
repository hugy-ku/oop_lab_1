import csv, os

# woah i might steal i mean borrow this
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany:")
germanies = []
for city in cities:
    if city["country"].lower() != "germany":
        continue
    germanies.append(city["city"])
print(germanies)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
hot_spains = []
for city in cities:
    if city["country"].lower() != "spain":
        continue
    if float(city["temperature"]) <= 12:
        continue
    hot_spains.append(city["city"])
print(hot_spains)
print()

# Count the number of unique countries
print("Number of unique countries:")
uniques = set()
for city in cities:
    if city["country"] not in uniques:
        uniques.add(city["country"])
print(len(uniques))
print()


# Print the average temperature for all the cities in Germany
print("Average temperature for all the cities in Germany:")
temps = []
for city in cities:
    if city["country"] != "Germany":
        continue
    temps.append(float(city["temperature"]))
print(sum(temps)/len(temps))
print()

# Print the max temperature for all the cities in Italy
print("Max temperature for all the cities in Italy:")
temps = []
for city in cities:
    if city["country"] != "Italy":
        continue
    temps.append(float(city["temperature"]))
print(max(temps))
print()