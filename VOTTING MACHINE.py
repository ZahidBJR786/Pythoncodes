print("imran for imran khan and nawaz for nawaz sharif")
PTI=0
PML=0
for x in range(20):
    a=input("please enter the vote: ")
    if a=="imran":
        PTI+=1
    elif a=="nawaz":
        PML+=1
    else:
        print("please enter right spelling")
print("Votes for IMRAN KHAN are: ",PTI)
print("votes for NAWAZ SHARIF are: ",PML)

