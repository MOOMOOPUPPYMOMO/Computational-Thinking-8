aura = 0 
furry = 0


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
elif answer == "B":
    furry += 1
    print("Damn...") 
else: 
    print("respond with A or B or else.....")
    furry += 3
