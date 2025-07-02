stud_dic = {'Alice':85,'Jay':70,'Harsh':80,'James':90}

name = input("Enter the student's name : ")

if name in stud_dic.keys():
    print(f"{name}'s marks : {stud_dic[name]}")
else:
    print("Student not found.")