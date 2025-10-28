import itertools
import random

count = 10000 # only possible if enough names or items to merge
file_name = "./exampleList.txt"

first = [
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

second = [
    "Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker",
    "Hoffmann", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder", "Neumann", "Braun",
    "Zimmermann", "Krüger", "Hartmann", "Schmid", "Lange", "Schmitt", "Werner", "Schmitz",
    "Krause", "Meier", "Lehmann", "Huber", "Mayer", "Kaiser", "Fuchs", "Lang", "Peters",
    "Vogel", "Scholz", "Jung", "Keller", "Herrmann", "Walter", "Roth", "Graf", "Beck",
    "Lorenz", "Winter", "Kraus", "Franke", "Schuster", "Schreiner", "Schwarz", "Kuhn"
    "Großmann", "Berschneider", "Frisch", "Moosburger", "Sommer", "Nasemann", "Herbert",
    "Schulz", "Mori", "Kim", "Wang", "Nguyen", "Daimler", "Merkel", "Erdmann", "Ebert"
    "Saotome", "Hatake", "Tsukino", "Henkel", "Klein", "Held", "Roronoa", "Katz", "Hundt",
    "Bub", "Weißmann", "Schwanz", "Seitz", "Peetz", "Altmann", "Reisch", "Fromm", "Hertz",
    "Hofer", "Zirbel", "Zimmermann", "Bimms", "Edelmaier", "Polster", "Markovka", "Platschek"
]

combinations = [f"{v} {n}" for v, n in itertools.product(first, second)]

random.shuffle(combinations)
unique_entry = combinations[:count]

with open(file_name, "w", encoding="utf-8") as f:
    f.write("\n".join(unique_entry))