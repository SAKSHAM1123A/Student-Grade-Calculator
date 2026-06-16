# Student-Grade-Calculator


# 🎓 Student Grade Calculator

A simple Python application that calculates a student's grade based on marks entered by the user. The program validates user input, assigns grades according to predefined grading criteria, and displays encouraging feedback messages.

## 📌 Project Overview

This project was developed as part of **Week 2: Making Decisions & Repeating Tasks in Python**. It demonstrates the use of:

* Conditional Statements (`if`, `elif`, `else`)
* Functions
* While Loops
* Input Validation
* User Interaction
* Python Fundamentals

The program accepts a student's name and marks, validates the input, calculates the appropriate grade, and displays a personalized result.

---

## 🚀 Features

* Accepts student name and marks.
* Validates marks input.
* Uses a function to calculate grades.
* Displays encouraging messages for each grade.
* Handles invalid inputs using a while loop.
* Simple and beginner-friendly code structure.

---

## 📝 Grading Logic

| Marks Range | Grade |
| ----------- | ----- |
| 90 - 100    | A     |
| 80 - 89     | B     |
| 70 - 79     | C     |
| 60 - 69     | D     |
| 0 - 59      | F     |

### Encouraging Messages

| Grade | Message                 |
| ----- | ----------------------- |
| A     | Great! Keep it up!      |
| B     | Very Good! Keep it up!  |
| C     | Good! Keep Improving!   |
| D     | Good! Keep Improving!   |
| F     | Focus more on Studying! |

---

## 📂 Project Structure

```text
Student-Grade-Calculator/
│
├── README.md
├── grade_calculator.py
└── screenshots/
```

---

## ⚙️ Requirements

* Python 3.x

No external libraries are required.

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone <repository-link>
```

### Navigate to Project Directory

```bash
cd Student-Grade-Calculator
```

### Run the Program

```bash
python grade_calculator.py
```

---

## 💻 Sample Output

```text
Enter Your Name:- Priya
Enter Your Marks:- 85

Result for Priya:-

Marks: 85/100
Grade: B
Message: Very Good! Keep it up!
```

---

## 🧪 Test Cases

| Input       | Expected Output |
| ----------- | --------------- |
| 95          | Grade A         |
| 85          | Grade B         |
| 75          | Grade C         |
| 65          | Grade D         |
| 40          | Grade F         |
| -5          | Invalid Marks   |
| 110         | Invalid Marks   |
| Empty Input | Ask Again       |

---

## 🎯 Learning Outcomes

Through this project, I learned:

* How to use conditional statements in Python.
* How to validate user input.
* How to create reusable functions.
* How to use loops for handling invalid data.
* How to build a real-world grading system.
* How to organize and document a Python project professionally.

---

## 👨‍💻 Author

**Saksham Bhatnagar**

Python Developer | Content Creator | Computer Science Enthusiast

---

## 📜 License

This project is created for educational and learning purposes.
