exampleList = []

with open("exampleList.txt", "r", encoding="utf-8") as f:
    for row in f:
        item = row.strip()
        if item:
            exampleList.append(item)

def linearSearch(list, key):
  index = 0
  while (index < len(list)):
    if (key == list[index]):
      return index
    index += 1
  return -1

if __name__ == "__main__":
  print(linearSearch(exampleList,"Ella Braun"))