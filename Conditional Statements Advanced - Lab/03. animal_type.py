animal_name = input()

if animal_name.lower() == "dog":
  print("mammal")
elif animal_name.lower() in ["crocodile", "tortoise", "snake"]:
  print("reptile")
else:
  print("unknown")
