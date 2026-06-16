Name = input("Enter Your name:- ")
Marks = (input("Enter Your Marks:- "))

while Marks =="" :
    print("Please enter your marks properly")
    Marks = (input("Enter Your Marks:- "))
else:
       Marks = int(Marks)

       
if Marks < 0 or Marks > 100:
        print("Please enter your marks properly")

elif Marks <= 59:
        print(f"Result for {Name}:- ")
        print(f"Marks: {Marks}/100")
        print("Grade: F")
        print("Message: Focus more on Studying!")

elif Marks <= 69:
        print(f"Result for {Name}:- ")
        print(f"Marks: {Marks}/100")
        print("Grade: D")
        print("Message: Good! Keep Improving!")

elif Marks <= 79:
        print(f"Result for {Name}:- ")
        print(f"Marks: {Marks}/100")
        print("Grade: C")
        print("Message: Good! Keep Improving!")

elif Marks <= 89:
        print(f"Result for {Name}:- ")
        print(f"Marks: {Marks}/100")
        print("Grade: B")
        print("Message: Very Good! Keep it up!")

else:
        print(f"Result for {Name}:- ")
        print(f"Marks: {Marks}/100")
        print("Grade: A")
        print("Message: Great! Keep it up!")