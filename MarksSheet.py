#from builtins import print

"""
Project Name: Student Marks Sheet Registration Form

Project Given as Part of Training in vnexgen
Trainer: Manoj
Author: Sandesh

"""

print ('-:Student Marks Sheet Registration Form:-')
a = int(input('Please Enter Number of Students: '))
b = 1
while b <= a:
    Name = input('Please Enter Student Name: ')
    Father_Name = input('Please Enter Father Name: ')
    Date_Of_Birth = input('Please Enter Student Date Of Birth: ')
    Class = input('Please Enter Class: ')
    Section = input('Please Enter Section: ')
    Sub_1 = int(input('Please Enter Marks for Sub_1: '))
    Sub_2 = int(input('Please Enter Marks for Sub_2: '))
    Sub_3 = int(input('Please Enter Marks for Sub_3: '))
    Sub_4 = int(input('Please Enter Marks for Sub_4: '))
    Sub_5 = int(input('Please Enter Marks for Sub_5: '))
    Sub_6 = int(input('Please Enter Marks for Sub_6: '))
    Total_Marks = (Sub_1 + Sub_2 + Sub_3 + Sub_4 + Sub_5 + Sub_6)
    print ('Total Marks Obtained for', Name, 'is', Total_Marks)
    if (Sub_1 > 35) and (Sub_2 > 35) and (Sub_3 > 35) and (Sub_4 > 35) and (Sub_5 > 35) and (Sub_6 > 35):
        print (Name , "You have Passed All the Subjects")
    elif (Sub_1 > 35) and (Sub_2 > 35) and (Sub_3 > 35) and (Sub_4 > 35) and (Sub_5 > 35) and (Sub_6 < 35):
        print (Name , "You Have Failed in Sub_6")
    elif (Sub_1 > 35) and (Sub_2 > 35) and (Sub_3 > 35) and (Sub_4 > 35) and (Sub_6 > 35) and (Sub_5 < 35):
        print (Name , "You Have Failed in Sub_5")
    elif (Sub_1 > 35) and (Sub_2 > 35) and (Sub_3 > 35) and (Sub_6 > 35) and (Sub_5 > 35) and (Sub_4 < 35):
        print (Name , "You Have Failed in Sub_4")
    elif (Sub_1 > 35) and (Sub_2 > 35) and (Sub_6 > 35) and (Sub_4 > 35) and (Sub_5 > 35) and (Sub_3 < 35):
        print (Name , "You Have Failed in Sub_6")
    elif (Sub_1 > 35) and (Sub_6 > 35) and (Sub_3 > 35) and (Sub_4 > 35) and (Sub_5 > 35) and (Sub_2 < 35):
        print (Name , "You Have Failed in Sub_2")
    elif (Sub_6 > 35) and (Sub_2 > 35) and (Sub_3 > 35) and (Sub_4 > 35) and (Sub_5 > 35) and (Sub_1 < 35):
        print (Name , "You Have Failed in Sub_1")
    else:
        print (Name, "You have Failed..!")
    average = Total_Marks/6 
    print (' Percentage of ', Name, 'is: ', average)
    if(average>=91 and average<=100):
    	print("Your Grade is A+");
    elif(average>=81 and average<=90):
    	print("Your Grade is A");
    elif(average>=71 and average<=80):
    	print("Your Grade is B+");
    elif(average>=61 and average<=70):
    	print("Your Grade is B");
    elif(average>=51 and average<=60):
    	print("Your Grade is C+");
    elif(average>=41 and average<=50):
    	print("Your Grade is C");
    elif(average>=36 and average<=40):
    	print("Your Grade is F");
    else:
    	print("You Have Failed..!!");
    b += 1