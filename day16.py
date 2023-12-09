print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1
while True:
  lyrics = input("Last Christmas I ____ you my heart. ")
  if lyrics == "gave":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "gave":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")