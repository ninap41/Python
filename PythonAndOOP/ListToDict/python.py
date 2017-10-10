name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1,arr2):

  dictionary = dict(zip(name,favorite_animal))
  print(dictionary)
  

make_dict(name,favorite_animal)