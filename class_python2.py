class Car:
  def __init__(self,name,model,year):
    self.name=name
    self.model=model
    self.year=year
  def __repr__(self):
    return f"{type(self).__name__}({self.name},{self.model},{self.year})"
  def __str__(self):
    return f"{type(self).__name__}({self.name},{self.model},{self.year})"

test=Car("benz",'550i',2003)
print(test)
print(type(test).__name__)


