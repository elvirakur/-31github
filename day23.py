def login():
  while True:
    username = input("Whatis your username?:")
    password = input("What is your password? ")
    if username == "Liana" and password == "Princess":
      print("Welcome Liana!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue
    
print("Liana LOGIN SYSTEM")
login()