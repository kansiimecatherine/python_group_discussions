   ##LISTS
                                          #BASICS   
#approach one
fruits = ['Apple','Pineapple','Water Melon','Mango','Orange']
for fruit in fruits:
    print(fruit)


#approach two

def juicy_fruits():
    fruits = ['Pawpaw','Passion fruit','Cherry','Mango','Straw berries']
    for fruit in fruits:
        print(f"\t{fruit}")
    
juicy_fruits()


                                        #INTERMEDIATE
#approach one
def SquareNumbers(numbers):
    

    square_numbers = [number**2 for number in numbers]
    return square_numbers

unsquared_numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
result = SquareNumbers(unsquared_numbers)

print(f"\nThe unsquared list of numbers is : {unsquared_numbers}")
print(f"\nThe squared list of numbers is : {result}",'\n\n')


#approach two.

def square_numbers(numbers):

    square = []
    for number in numbers:
        square.append(number ** 2)
    return square

    
original_list = [10,20,30,40,50]
squared_list = square_numbers(original_list)

print(f"\nThe unsquared list of numbers is : {original_list}")
print(f"\nThe squared list of numbers is : {squared_list}",'\n\n')



                           #ADVANCED
#approach one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = []

for number in range(len(list1)):
    combined.append(list1[number])  # Append element from list1
    combined.append(list2[number])  # Append element from list2

print("The Combined List is :", combined)



# #approach two
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Initialize an empty list to hold the combined elements
combined = []

# Use a loop to interleave elements from list1 and list2
for a, b in zip(list1, list2):
    combined.extend([a, b])

print("Combined List:", combined)

                           
                           
                           
                            #CHALLENGE


#approach one
numbers = [3, 1, 4, 1, 5, 9, 2] #list of numbers
largest_numbers = numbers[2]
for number in numbers[1:]: #slicing to end
    if number > largest_numbers:
        print("The largest number is : ",number,'\n\n')

#approach two
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort(reverse=True) 
print(f"The two largest numbers are {numbers[0]} and {numbers[1]}")

















