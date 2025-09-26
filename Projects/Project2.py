aura = 0 
furry = 0
steve = 0


answer = input("what gender you Male or Female? A) Male, or B) Female")
if answer == "A":
    furry += 1
    print("sure...")
elif answer == "B":
    aura += 1
    print("ok...sure") 
else: 
    print("respond with A or B or else.....")
    furry += 3
answer = input("Do you play basketball? A) Yes, or B) No")
if answer == "A":
    furry += 1
    print("Not a fan personally...")
elif answer == "B":
    aura += 1
    print("YES SAME!!!") 
else: 
    print("respond with A or B or else.....")
    furry += 3
answer = input("What do you prefer? A) Dogs, or B) Garfield")
if answer == "A":
    aura += 1
    print("Sure idc...")
elif answer == "B" :
    furry += 1
    print("Damn...") 
else: 
    print("respond with A or B or else.....")
    furry += 3
answer = input("What do you prefer? A) Soccer, or B) Lacrosse")
if answer == "A" or answer == "a":
    aura += 1
    print("cool...")
elif answer == "B" or answer == "b":
    furry += 1
    print("you have bad taste...") 
else: 
    print("respond with A or B or else.....")
    furry += 3
answer = input("What do you prefer? A) Pizza, or B) Burgers, or C) Wings")
if answer == "A" or answer == "a":
    aura += 1
    print("Ok...")
elif answer == "B" or answer == "b":
    furry += +1
    print("Ehh...") 
elif answer == "C" or answer == "c":
    steve += 1000000
else: 
    print("respond with A or B or else.....")
    furry += 3
# end of quiz:
print ("calculating results...")
if aura > furry and aura > steve:
    print ("you are a ladies man!")
if furry > aura and furry > steve:
    print ("you are a furry")
if steve > aura and steve> furry:
    print ("you like chicken wings")
