city = "  nEw   dELhi  "

city = city.strip()
city = " ".join(city.split())

if all(char.isalpha() or char == " " for char in city):
    print(city.title())
else:
    print("Invalid city")