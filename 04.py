# string
name = "Arne"

#integer
zahl = 42

# float
pi = 3.14

# bool
wahr = True
falsch = False

eingabe = input("nenne mir bitte eine Zahl: ")

if int(eingabe) == zahl:
  print("Deine Zahl ist 42.")
elif int(eingabe) == 23:
  print("23 ist auch eine schöne Zahl.")
elif int(eingabe) == 9:
  print("9 ist auch eine nette Zahl.")
else:
  print("du hast eine andere Zahl gewählt.")

def malZwei(x):
  return 2*x

print("Lass uns ein wenig rechnen. Fangen wir mit der Multiplikation mit 2 an.")
eingabe = input("wie lautet deine Zahl? ")
zahl = int(eingabe)

print("2 x "+eingabe +" = "+str(malZwei(zahl)))