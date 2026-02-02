a = 1
b = a+1
count = 0
while count < 10:
  result = a + b
  print(f"{a} + {b} = {result}")
  a = result
  b = result + 1
  count = count + 1