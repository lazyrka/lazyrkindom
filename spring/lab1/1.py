a = list()
word = input()
while word != '':
  a.append(int(word))
  word = input()
a.sort()
if len(a) % 2 == 0:
  b = (a[len(a)//2-1]+a[len(a)//2])/2
  print(float(b))
elif len(a) % 2 == 1:
  print(float(a[(len(a)-1)//2]))
