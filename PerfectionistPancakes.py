'''
1. Flow diagram for onePlatetoAnother() - See Paper
2. The output for this would be ['choco chip', 'strawberry', 'blueberry']
3. The base case for this is if the length of pancakes is 0, then the return will be an empty list
4. The output for main in this case would be Your order of ['birthday cake', 'strawberry', 'maple'] is up!
'''


#input: user input
#output: user input
def takeOrders():
    return input("What would you like today?\n")

#input: string of comma-separated types of pancakes
#output: list of types of pancakes
#ex: input: "rice, whole wheat, chocolate" output: [“rice”, “whole wheat”, “chocolate”]
def separateOrders(str):
    if (str.find(",") == -1):
        return [str]
    return [str[: str.find(",")]] + separateOrders(str[str.find(",") + 2:])
		

#input: pancakes–a list that contains a stack of pancakes
#output: you answer :)
def onePlateToAnother(pancakes):
    if(len(pancakes) == 0):
	    return []
    else:
	    return [pancakes[len(pancakes)-1]] + onePlateToAnother(pancakes[:len(pancakes) - 1])

print('TESTING:', onePlateToAnother(['blueberry', 'strawberry', 'choco chip']))
order = []

def orderUp(totalNum, orders): 
    #your code here!
    if totalNum == 0:
        return order
    order[totalNum - 1] = separateOrders(orders[totalNum - 1])

    return

#What is this function doing?
def main():
    pancakeStack = [takeOrders()]
    while(input("Would you like anything else? y/n\n").lower() != "n"):
	    pancakeStack.append(takeOrders())
    madeOrder = onePlateToAnother(pancakeStack)
    print("Your order of {} is up!".format(madeOrder))

if __name__ == "__main__":
    main()
