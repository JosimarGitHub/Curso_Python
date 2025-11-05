from restaurant import Restaurant

restaurant = Restaurant('pertinho de minas','comida mineira')

print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()