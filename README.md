# Lab10PerfectionistPancakes
Recursion Warmup Lab

You have been hired as a new employee at a perfectionist-run cafe. The owners are very particular about how they like things organized, so they have decided to implement a robot to do some of the work for them. You are in charge of coding the robot. Here is some of the code you have already written:

def takeOrders():
    return input("What would you like today?\n")

#input: string of comma-separated types of pancakes
#output: list of types of pancakes
#ex: input: "rice, whole wheat, chocolate" output: [“rice”, “whole wheat”, “chocolate”]
def separateOrders(str):
    lst = []
    if (str.find(",") == -1):
        return [str]
    return [str[: str.find(",")]] + separateOrders(str[str.find(",") + 1:])
		

#input: pancakes–a list that contains a stack of pancakes
#output: you answer :)
def onePlateToAnother(pancakes):
    if(len(pancakes) == 0):
return []
    else:
return [pancakes[len(pancakes)-1]] + onePlateToAnother(pancakes[:len(pancakes) - 1])

#What is this function doing?
def main():
    pancakeStack = [takeOrders()]
    while(input("Would you like anything else? y/n\n").lower() != “n”):
pancakeStack.append(takeOrders())
    madeOrder = onePlateToAnother(pancakeStack)
    print("Your order of {} is up!".format(madeOrder))

if __name__ == "__main__":
    main()



Read through the code and answer the following questions:
What is the output for onePlateToAnother?
	A list that contains pancakes in reverse order

What is the output for onePlateToAnother([“blueberry”, “strawberry”, “choco chip”]?
	[“choco chip”, “strawberry”, “blueberry”]

What is main() doing?
	Main takes an order from standard input until the user enters “n”. Then it reverses the list and prints “Your order of (madeOrder) is up!”

What is the output for main() when this is the input?:
maple
Y
strawberry 
y 
birthday cake
n 
double chocolate

Your order of [“birthday cake”, “strawberry”, “maple”] is up!



Now it’s your turn! Write a function that takes in the initial number of orders and a list of orders (this will be a list of strings) and then RECURSIVELY prints each order and says “Order #___, your order of ___ pancakes is up!”
Example of how this function would be used: orderUp(3, [“blueberry, strawberry”, “plain, whole wheat”, “banana nut, birthday cake, chocolate cake”])
(the output would be:
“Order #1, your order of [“blueberry”, “strawberry”] pancakes is up!”
“Order #2, your order of [“plain”, “whole wheat”] pancakes is up!”
“Order #3, your order of [“banana nut”, “birthday cake”, “chocolate cake”] pancakes is up!” )
(Hint: there is already a function for turning strings into lists)
	
def orderUp(totalNum, orders):
	#your code here!

Sample orderUp(totalNum, orders):

def orderUp(totalNum, orders):
    if len(orders) == 0:
        return
    flipped = onePlateToAnother(separateOrders(orders[0]))
    print("Order #{}, your order of {} pancakes is up!".format(totalNum - len(orders) + 1, flipped))
    orderUp(totalNum, orders[1:])
