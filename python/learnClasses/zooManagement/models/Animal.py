class Animal:
  name: str
  species: str
  age: int
  weight: float

  def __init__(self, name: str, species: str, age: int, weight: float):
    self.name = name
    self.species = species
    self.age = age
    self.weight = weight

  def feed(self, kg: float) -> None:
    if kg <= 0:
      raise ValueError("Die angegebene Angabe muss über 0 Kg sein.")
    self.weight += kg

  def description(self) -> str:
    return "Dies ist eine allgemeine Tierart, die einen Namen, ein Alter und ein Gewicht enthält."