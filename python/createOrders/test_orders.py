from order_manager import OrderManager

test = OrderManager()

def test_order_id() -> bool:
  checks_ok = False

  try:
    test.add_order(1, 1.5)
    checks_ok = True
  except Exception as e:
    checks_ok = False

  try:
    test.add_order(None, 1)
    checks_ok = False
  except Exception as e:
    checks_ok = True

  try:
    test.add_order([1,2,3], 1)
    checks_ok = False
  except Exception as e:
    checks_ok = True

  return checks_ok

def test_order_value() -> bool:
  checks_ok = False

  try:
    test.add_order(1, 2.7)
    checks_ok = True
  except Exception as e:
    checks_ok = False

  try:
    test.add_order(1, 0)
    checks_ok = False
  except Exception as e:
    checks_ok = True
  
  try:
    test.add_order(1, None)
    checks_ok = False
  except Exception as e:
    checks_ok = True

  try:
    test.add_order(1, "a")
    checks_ok = False
  except Exception as e:
    checks_ok = True
  
  return checks_ok

if __name__ == "__main__":
  # Prüfung von Order-ID
  if test_order_id():
    print("✓ Order-ID wird korrekt verarbeitet")
  else:
    print("𐄂 Order-ID wird nicht korrekt verarbeitet")

  # Prüfung von Order-Value
  if test_order_value():
    print("✓ Order-Value wird korrekt verarbeitet")
  else:
    print("𐄂 Order-Value wird nicht korrekt verarbeitet")

  # Prüfung der gesamten Werte (Erster Test in Testfunktionen wird korrekt verarbeitet, die Summe daraus muss hier erscheinen)
  if test.total_order_value() == 4.2:
    print("✓ Gesamtbetrag wird korrekt ausgegeben")
  else:
    print("𐄂 Gesamtbetrag wird nicht korrekt ausgegeben")