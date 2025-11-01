# Description
I have a given haskell-code
```haskell
sumList :: [Integer] -> Integer
sumList[] = 0
sumList(x:xs) = x + sumList(xs)
```

and this code was translated into a python programm.