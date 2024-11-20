                            #DICTIONARIES

                          ##BASICS 
student_details = {
    'name':'KANSIIME CATHERINE',
    'age':20,
    'grade':'A'
}
for key,value in student_details.items():
    print(f"{key} : {value}")



                   ##INTERMEDIATE

#approach one
def older_people(people):
    # List comprehension to get names of people who are 21 or older
    adults = [name for name, age in people.items() if age >= 21]

    return adults

#creating a dictionary
people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}

# Calling  the function
adults = older_people(people)

print(adults)

#approach two

def old_people():
    adults = []
    people_database = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
    for name, age in people_database.items():
        if age >= 21:
            adults.append(name)
            print(f"\nThe adults are {adults}",'\n\n')
old_people()
               #ADVANCED


def calculate_total_cost(items_bought, store_prices):

    total_cost = 0
    
    for item in items_bought:
        if item in store_prices:
            total_cost += store_prices[item]
    
    return total_cost

store_prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
items_bought = ['apple', 'orange', 'banana', 'banana']

total_cost = calculate_total_cost(items_bought, store_prices)

print(f"The total cost of items bought is: shs.{total_cost:.2f}",'\n\n')


                           #CHALLENGE
def count_words(sentence):
    # Convert the sentence to lowercase and split it into words
    words = sentence.lower().split()
   
    # Initialize an empty dictionary to store word counts
    word_count = {}
   
    # Loop through each word in the list of words
    for word in words:
        # Remove any punctuation from the word
        word = word.strip(",.?!;:")
       
        # Update the count of the word in the dictionary
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
   
    return word_count

#using the sentence below
sentence = "hello everyone , hello people . Hello Uganda , my home Uganda . "

# Call the function and print the result
result = count_words(sentence)
print(result)




