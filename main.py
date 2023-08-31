keep_going=True
data=[]
grades=[]
#starts loop to input the student information
while keep_going:
    name = input("What is the student's name?\n")

    try:
        #checks if input of student name is a string. If the input is not a letter it prints out an error message and stops the program
        name=str(name).title()
    except ValueError:
        print("Name is incorrect\nRestart the program")
        break
    grade=input("What is the student's grade?\n")
    try:
        # checks if input of student grade is a number. If the input is not a number it prints out an error message and stops the program
        grade=round(float(grade),2)
    except ValueError:
        print("The grade is not a number\nRestart the program")
        break
    if grade>100:
        print("The grade is not less than 100.\nRestart the program")
        break
    data.append({"name":name,"grade":grade})
    #gives a choice to user to stop inputting student information
    going=input("Do you want to continue adding students grades?\nType 'no' to stop.\n")
    if going=="no" or going=="n":
        keep_going=False
for person in data:
    #loops through the list in order to assign a grade to the student and adds it to a new list
    if person["grade"]<40:
        state="Fail"
    elif person["grade"]<50:
        state="Pass"
    elif person["grade"]<60:
        state="2:2"
    elif person["grade"]<70:
        state="2:1"
    else:
        state="Honours"
    grades.append({"name":person["name"],"grade":state,"score":person["grade"]})

for person in grades:
    #prints out message of name and grade and if they passed
    if person["grade"]=="Fail":
        print(f"{person['name'].title()} failed the course with a score of {person['score']}0/100")
    else:
        print(f"{person['name'].title()} got a {person['grade']}. They had a score of {person['score']}0/100")
