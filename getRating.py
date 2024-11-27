import csv
from collections import defaultdict

# Initialize a dictionary to store the sum of ratings and count for each food item
ratings = defaultdict(lambda: {'sum': 0, 'count': 0})

# Read the CSV file
with open('unscrambled_ratings.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        food = row['item']
        rating = int(row['rating'])  # Convert rating to an integer
        ratings[food]['sum'] += rating
        ratings[food]['count'] += 1

# Calculate averages and find the highest
highest_avg = None
highest_food = None

for food, values in ratings.items():
    avg_rating = values['sum'] / values['count']
    if highest_avg is None or avg_rating > highest_avg:
        highest_avg = avg_rating
        highest_food = food

# Output the food item with the highest average rating
print(f"The food item with the highest average rating is {highest_food} with an average rating of {highest_avg:.2f}")
