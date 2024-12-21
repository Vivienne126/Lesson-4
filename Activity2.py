Amount=int(input("Enter your amount"))
note1=Amount//100
note2=(Amount%100)//50
note3=((Amount%100)%50)//10

print("number of notes of hundread are", note1)
print("number of notes of fifty are", note2)
print("number of notes of ten are", note3)