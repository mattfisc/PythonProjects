import random

class MyNumbers:
  def __iter__(self):
    self.a = 2
    return self

  def __next__(self):
    x = self.a
    self.a += random.randint(2,10)
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))