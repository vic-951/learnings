from .Animal import Animal

class Herbivore(Animal):
  prefered_plants = str

  def __init__(self, name: str, species: str, age: int, weight: float, prefered_plants: str):
    super().__init__(name, species, age, weight)
    self.prefered_plants = prefered_plants
  
  def description(self) -> str:
    return "Dies ist ein Pflanzenfresser, der einen Namen, ein Alter, ein Gewicht und die bevorzugte pflanzliche Nahrungsquelle enthält."