# Lab10PerfectionistPancakes
Recursion Warmup Lab

# Attached is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students, and seek better understanding to these questions. See below for reminders on types, variables, and input.

# Scenario
You have been hired as a new employee at a perfectionist-run cafe. The owners are very particular about how they like things organized, so they have decided to implement a robot to do some of the work for them. You are in charge of coding the robot. Attached is some of the code you have already written.

# Step 1
1. What is the output for onePlateToAnother?
2. What is the output for onePlateToAnother([“blueberry”, “strawberry”, “choco chip”]?
3. What is main() doing?
4. What is the output for main() when this is the input?:
maple
Y
strawberry 
y 
birthday cake
n 
double chocolate

# Step 2: Coding orderUp(totalNum, orders)
Now it’s your turn! Write a function that takes in the initial number of orders and a list of orders (this will be a list of strings) and then RECURSIVELY prints each order and says “Order #_, your order of _ pancakes is up!”

For Example, for orderUp(3, \[“blueberry, strawberry”, “plain, whole wheat”, “banana nut, birthday cake, chocolate chip”])
the output would be: \n
“Order #1, your order of \[“blueberry”, “strawberry”\] pancakes is up!” \n
“Order #2, your order of \[“plain”, “whole wheat”] pancakes is up!” \n
“Order #3, your order of \[“banana nut”, “birthday cake”, “chocolate chip”] pancakes is up!” \n
(Hint: there is already a function for turning strings into lists)

# Step 3: Test orderUp(totalNum, orders)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().

print("TESTING", orderUp(3, \[“blueberry, strawberry”, “plain, whole wheat”, “banana nut, birthday cake, chocolate chip”]))
Also add your own tests!

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on Lists


# Reminder on Using Functions Within Functions

# Reminder on Recursion
