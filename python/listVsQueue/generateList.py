import itertools
import random

count = 1000000
file_name = "./exampleList.txt"

request = [
    "hinzufügen","hinzufügen","hinzufügen","entfernen"
]

value = [
    "Anna", "Ben", "Clara", "David", "Ella", "Felix", "Greta", "Hannah", "Jonas", "Klara",
    "Leon", "Mia", "Noah", "Oskar", "Paula", "Quentin", "Rosa", "Simon", "Tina", "Uwe", "Usagi",
    "Viktor", "Wanda", "Xaver", "Yara", "Zoe", "Sarah", "Lukas", "Tim", "Laura", "Nico",
    "Emma", "Lena", "Tom", "Sophie", "Philipp", "Lea", "Moritz", "Julian", "Eva", "Fabian", 
    "Otto", "Michael", "George", "Luisa", "Benjamin", "Aaron", "Frederyk", "Georgina", "Belacky", 
    "Blake", "Jayqualin", "Jaqueline", "Timothy", "Waldemar", "Patricia", "Sabrina", "Denise", 
    "Denice", "Chan", "Kasula", "Conan", "Kogoro", "Erika", "Erwin", "Angelina", "Katja", "Helene", 
    "Martha", "Jan", "Sybille", "Franz", "Bruno", "Yildrim", "Franklin", "Beate", "Robyn", "Amala", 
    "Stephanie", "Hans-Peter", "Rüdiger", "Son Goku", "Boris", "Rita", "Manni", "Jürgen", "Enis"
    "Ran", "Ranma", "Denji", "Akane", "Makima", "Nami", "Zoro", "Brook", "Franky", "Rambo",
    "Gudrun", "Francois", "Sasuke", "Kakashi", "Mamoru", "Amy", "Vivian", "Valeria", "Wowa"
]

request_list = []

for i in range(count):
  request_item = random.choice(request)
  value_item = random.choice(value)
  request_list.append(request_item + " " + value_item)

with open(file_name, "w", encoding="utf-8") as f:
    f.write("\n".join(request_list))