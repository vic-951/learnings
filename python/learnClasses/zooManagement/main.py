from zooManagement import Animal, Preditor, Herbivore

anton = Animal("Anton", "Braunbär", 14, 232.4)
boris = Preditor("Boris", "Löwe", 9, 80.6, "Antilopen")
lisa = Herbivore("Lisa", "Elefant", 46, 634.9, "Früchte")

def showAnimals():
  print("================================================================")
  print("================== Übersicht der Tiere im Zoo ==================")
  print("================================================================")
  print(f"Name: {anton.name}")
  print(f"Spezies: {anton.species}")
  print(f"Alter: {anton.age}")
  print(f"Gewicht: {anton.weight}")
  print(f"Beschreibung: {anton.description()}")
  print("================================================================")
  print(f"Name: {boris.name}")
  print(f"Spezies: {boris.species}")
  print(f"Alter: {boris.age}")
  print(f"Gewicht: {boris.weight}")
  print(f"Beuteart: {boris.prefered_prey}")
  print(f"Beschreibung: {boris.description()}")
  print("================================================================")
  print(f"Name: {lisa.name}")
  print(f"Spezies: {lisa.species}")
  print(f"Alter: {lisa.age}")
  print(f"Gewicht: {lisa.weight}")
  print(f"Beuteart: {lisa.prefered_plants}")
  print(f"Beschreibung: {lisa.description()}")

def feed_animals():
  anton.feed(6.2)
  boris.feed(4.4)
  lisa.feed(12.6)

if __name__ == "__main__":
  showAnimals()
  feed_animals()
  showAnimals()