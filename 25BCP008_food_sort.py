food = [
    ("Pizza", 500),
    ("Burger", 200),
    ("Pasta", 400),
    ("Fries", 150)
]

for i in range(len(food)):
    for j in range(i + 1, len(food)):
        if food[i][1] < food[j][1]:  
            food[i], food[j] = food[j], food[i]

print(food)
