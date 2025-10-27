def getDevider(a, b):
  answer = 1
  devider = 2

  while ((devider <= a) and (devider <= b)):
    if (((a % devider) == 0) and ((b % devider) == 0)):
      answer = devider
    devider += 1
  
  return answer


if __name__ == "__main__":
  a = eval(input('Please gimme a number: '))
  b = eval(input('Gimme another number: '))
  print(getDevider(a,b))