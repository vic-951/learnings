from collections import deque

def sumList(numbers: list[int]) -> int:
  if not numbers:
    return 0
  
  queue = deque(numbers)
  x = queue.popleft()
  return x + sumList(queue)

if __name__ == "__main__":
  print(sumList([]))
  print(sumList([4,7,2]))
  print(sumList([4,7,2,8,12,2,3,4,5,6,3,1,1,2,4,3,4,5,6]))