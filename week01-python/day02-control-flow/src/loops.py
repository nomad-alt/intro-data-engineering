for number in range(5):
    print(number)

cities = ["Stockholm", "London", "Tokyo"]

for city in cities:
    print(city)

count = 1

while count <= 5:
    print(count)
    count += 1

for number in range(10):
    if number == 5:
        break
    print(number)

for number in range(10):
    if number == 3:
        continue
    print(number)

for number in range(11):
    if number % 2 == 0:
        print(number)
