def factorial(n: int) -> int:
  if n < 0:
    raise ValueError("n muss größer gleich 0 sein.")
  
  if n == 0:
    return 1
  
  return n * factorial(n - 1)

if __name__ == "__main__":
  print(factorial(0))
  print(factorial(1))
  print(factorial(1+1))
  print(factorial(6))
  