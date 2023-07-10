
import time


print("Hallo, User.")

print("Frage 1: Wie ist Ihr Name?")
time.sleep(10)
username = input("Geben Sie jetzt Ihren Namen ein: ")
print("Herzlich Willkommen, " + username + "!")


print("Frage 2: Wie geht es Ihnen " + username + "? " )
time.sleep(10)
frage2 = input("Antwort: ")
if frage2 == "Gut" or "gut":
    print("Das freut mich " + username + "!")
    
elif frage2 == "Schlecht" or "schlecht":
    print("Oh Schade. Ich wünsche Ihnen eine gute Besserung " + username + "!")


else:
    print("Leider konnte Ihre Eingabe nicht berücksichtigt werden!")


print("Frage 3: Was sind Ihre Hobbys?")
time.sleep(10)
frage3 = input("Nennen Sie Ihre Hobbys " + username + "? ")
print("Ihre Hobbys sind: " + frage3 + ".")

    
print("Frage 4: Welche Sportart supporten Sie? ")
time.sleep(10)
frage4 = input("Geben Sie eine Sportart an die Sie supporten: ")




print("Frage 5: Wer ist Ihr Lieblingssportler/In?")
time.sleep(10)
frage5 = input("Geben Sie Ihre Antwort ein: ")
print("Sie haben " + frage5 + " gewählt.")



print("Frage 6: Sind Sie ein fauler Mensch?")
time.sleep(10)
frage6 = input("Antwort: ")

if frage6 == "ja":
    print("Hahahaha")
    
elif frage6 == "nein":
    print("Hahah, das ist gut das Sie nicht faul sind.")
    
else:
    print("Eingabe ungültg!")
    

print("Frage 7: Haben Sie berufliche Erfahrungen? ")
time.sleep(10)
frage7 = input("Antwort: ")

if frage7 == "ja":
    print("Schön, das Sie Erfahrungen im beruflichen Leben sammeln konnten!")
elif frage7 == "nein":
    print("Schade!")
else:
    print("Eingabe ungültig!")
    
    
print("Frage 8: Was sind Ihre Stärken?")
time.sleep(10)
frage8 = input("Geben Sie Stärken jetzt an: ")

print("Frage 9: Was sind Ihre Schwächen?")
time.sleep(10)
frage9 = input("Geben Sie Ihre Schwächen jetzt an: ")


print("Frage 10:Was Ihr Lieblingsessen?")
time.sleep(10)
frage10 = input("Antwort: ")
print("Ihr Lieblingsessen ist: " + frage10 + ".")

print("Frage 11: Was Ihre Lieblingsfarbe?")
time.sleep(10)
frage11 = input("Antwort: ")
print("Ihre Lieblingsfarbe ist: " + frage11 + ".")
    
