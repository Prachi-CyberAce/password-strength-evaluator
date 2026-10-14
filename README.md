**Password Strength Evaluator**

A beginner-friendly Python cybersecurity project that evaluates password strength and provides tips to improve password security.

**About the Project**

The Password Strength Evaluator is a command-line tool built with Python. It checks a password using different criteria and gives a score out of 100, a strength rating and suggestions for improvement.

The program hides password input while typing and does not save or send passwords anywhere.

**Features**
Password scoring: Assigns a score from 0 to 100.

Strength rating: Categorizes passwords as Very Weak, Weak, Okay, Strong or Very Strong.

Length checking: Rewards longer passwords.

Character variety: Checks for lowercase letters, uppercase letters, numbers and symbols.

Common password detection: Identifies passwords in a small built-in list of commonly used passwords.

Sequence detection: Flags patterns such as abcd, 1234 and qwer.

Repeated character detection: Flags patterns such as aaa and 111.

Entropy estimation: Calculates an approximate entropy value based on password length and character variety.

Security feedback: Provides suggestions for improving password strength.

Hidden input: Uses Python's getpass module to hide password input in the terminal.

**Technologies Used**

Python 3.8+

math module

string module

getpass module

No additional libraries are required.

**How to Run**

1. Install Python

Download Python from the official website:

https://www.python.org/downloads/

2. Download this project

Clone the repository:

git clone https://github.com/Prachi-CyberAce/password-strength-evaluator.git

Alternatively, download the repository as a ZIP file from GitHub.

3. Open the project folder

Open Command Prompt or a terminal inside the project folder.

4. Run the program

python password_evaluator.py

On some Windows systems, you may need to use:

py password_evaluator.py

5. Test a password

Enter a test password when prompted. The program displays a score, a strength label, an estimated entropy value and any relevant suggestions.

Press Enter without entering a password to exit.

**Cybersecurity Concepts Learned**

Password security fundamentals

Password length and character diversity

Common password patterns

Basic password entropy estimation

Input handling in Python

Conditional statements, loops, functions and sets

**Limitations**

The common-password list is small and does not represent a comprehensive password database.

The entropy value is a simplified estimate, not a guarantee of real-world password security.

The score is a basic educational heuristic, not a professional password-security assessment.

This tool does not check passwords against leaked-password databases or online services.

This project is intended for educational purposes and should not be used as the sole method for evaluating real-world password security.

**Author**

Prachi Raut

GitHub: Prachi-CyberAce

**If you find this project useful, consider giving the repository a star!**
