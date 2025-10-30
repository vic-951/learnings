from typing import Hashable, Dict

class OrderManager:

  def __init__(self) -> None:
    self._orders: Dict[Hashable, float] = {}
  
  @staticmethod
  def is_hashable(value) -> bool:
    try:
      hash(value)
    except TypeError:
      return False
    return True

  def add_order(self,order_id: Hashable, order_value: float) -> None:
    if order_id is None:
      raise ValueError("order_id darf nicht None sein.")
    if not self.is_hashable(order_id):
      raise ValueError("order_id muss hashable sein, es darf kein list, dict oder set sein.")
    if order_value is None:
      raise ValueError("order_value darf nicht None sein.")
    if not isinstance(order_value, (int,float)):
      raise ValueError("order_value muss eine gültige Zahl sein.")
    if order_value <= 0:
      raise ValueError("order_value muss größer als 0 sein.")
    
    if order_id in self._orders:
      self._orders[order_id] += float(order_value)
    else:
      self._orders[order_id] = float(order_value)

  def total_order_value(self) -> float:
    return float(sum(self._orders.values()))
    