#>>1
str ="Hello World"
reverse_list=[word[::-1] for word in str.split(" ")]
res=' '.join(reverse_list)
print(res)

#>>2
str="PACE Wisdom"
lower_count=0
upper_count=0
for letter in str:
    if letter.islower():
        lower_count=lower_count+1
    elif letter.isupper():
        upper_count=upper_count+1
print(lower_count)
print(upper_count)

#>>3
def printfibonacci(a, b):
  fib_series = []
  x, y = 0,1
  while y<b:
   fib_series.append(y)
   x,y = y, x+y
  for i in fib_series:
    if i>a:
        print(i)
printfibonacci(10,150)

#>>5
import pandas as pd
data = pd.read_csv(r"C:\Users\Nishchit\Documents\Py5.csv", sep=",")
print("Student Name","total marks","average marks")
for x in data.values:
  total = x[1]+x[2]+x[3]+x[4]
  avg = total/4
  print(x[0], total, avg)


