from .Animal import Animal

class Preditor(Animal):
  prefered_prey = str

  def __init__(self, name: str, species: str, age: int, weight: float, prefered_prey: str):
    super().__init__(name, species, age, weight)
    self.prefered_prey = prefered_prey

  def description(self) -> str:
    return "Dies ist eine Raubtier, welches einen Namen, ein Alter, ein Gewicht und die Beuteart enthält."