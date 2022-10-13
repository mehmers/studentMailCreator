count = 0
while count > -1 :
  lookup = {
    "ü" : "u",
    "Ü" : "u",
    "Ş" : "s",
    "ş" : "s",
    "ı" : "i",
    "İ" : "i",
    "Ç" : "c",
    "ç" : "c",
    "Ğ" : "g",
    "ğ" : "g",
    "ö" : "o",
    "Ö" : "o",
  }

  name = input("Enter name and surname (-1 to exit) : ")
  if(name == "-1"):
    print("Loop terminated with " + str(count) + " mail conversations")
    break

  newName = ""
  for letter in name:
    if lookup.get(letter) != None :
      newName = newName + lookup.get(letter)
    else :
      newName = newName + letter

  newName = newName.lower()
  newName = newName.split(" ")

  if len(newName) > 2:
    newName = newName[0] + " " + newName[len(newName)-1]
    newName = newName.split(" ")

  newName = " ".join(newName)
  mail = newName.replace(" ", ".") + "@std.antalya.edu.tr"
  print(mail)
  count +=1

