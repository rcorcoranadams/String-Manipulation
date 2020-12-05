# Rachel Corcoran-Adams
# September 25, 2020
# This exercise writes a function that capitalizes the first and fourth letters of a name.

# This line defines the function old_macdonald
def old_macdonald(name):
  # This line splits up the first half of the name
  str1 = name[0:3]
  # This line splits up the second half of the name
  str2 = name[3:]
  # This line capitalizes the first letter of the name
  str1=str1.capitalize()
  # This line capitalizes the fourth letter of the name
  str2=str2.capitalize()
  # This line prints and concatenates the two halves of the name
  print(str1+str2)
# This line returns and inputs the function
old_macdonald("macdonald")
