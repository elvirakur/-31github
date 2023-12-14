print("Welcome to Multiplication table Game")
print()
print("How well do you know your Multiplication table? Pick a number and I will give you 10 Multiplication table to solve.")
print()

fact_family = int(input("Name your multiples: "))
print()

counter = 0
for i in range(1, 11):
  correct_answer = i*fact_family
  print(i, "x", fact_family)
  answer = int(input("> "))
  if answer == correct_answer:
    print("Great work!")
    counter += 1
  else:
    print("Nope. The answer was", correct_answer)
if counter == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You scored", counter, "out of 10 correct.")