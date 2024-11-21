# # LOOPS


                                         # Basics
# # approach one
def even_number():
    for even in range(1,20):
        if even % 2 ==0:
            print(even)
even_number()
    
# #approach two 

def EvenNumbers():
    for numbers in range(2,21,2): # where 2 is the start,21 is the stop but its not includable,
        #the 2 is the step which outputs the second number
        print('\n',numbers)
EvenNumbers()


                                         # #Intermediate
                                         
# #approach two
def number():
    num = 0
    while num <= 10:
        num = int(input("Please enter a number : "))
        if num <= 10:
            print(f"\nYou have entered: {num}\n")
    
    print(f"\nThank you, number {num} is greater than 10.\n")

number()

                                    #Advanced
# A nested loop is a loop inside another loop(outer loop and inner loop)
for num1  in range(1, 6): #loop for numbers from 1 to 5 (outer loop)
    print(f"\nMultiplication Table for {num1}:",'\n\n')
    
    for num2 in range(1, 11): # This multiplies from 1 to 10.(inner loop)
        result = num1 * num2
        print(f"{num1} x {num2} = {result}")
    


                                       #Challenge
def sum_of_odd_numbers():  
                                    
    integers = [4, 7, 2, 9, 12, 15]
    sum = 0 #initial
    for number in integers:
        if number %2 !=0:
            sum+=number
    print(f"\nThe sum of all odd numbers is: {sum}",'\n\n')

sum_of_odd_numbers()
