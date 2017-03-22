color = "green"

def checkColor(color):
  checkColor = input("Is " + color + " your favorite color? ")
  if checkColor.lower() == "yes":
    print("That's my favorite too")
  else:
    color = input("What's your favorite color? ")
    print("Your favorite color is", color)

checkColor(color)
