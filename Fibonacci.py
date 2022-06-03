# recursive approach

numTerms = int(input("How many terms of Fibonacci to print?"))

# what r the first few terms of the Fibonacci seq?
# 0 1 1 2 3 

# main method
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n -1) + fibonacci(n - 2))

# check if the numbers of terms is actually valid
if numTerms <= 0:
    print ("please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(numTerms):
        print(fibonacci(i))


    





