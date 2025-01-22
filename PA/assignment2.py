 #Extract the names of all suggested cities for the ice cream store and count the number of letters in each city name.
#Topics: str, int
#Example Output: City: Miami, Letters: 5

cites= ["Miami","olathe","reston"]
for city in cites:
    print(f"city : {city} , letters : {len(city)}") 


#Identify the suggested ice cream flavors and calculate the average length of the flavor names.


flavors=["vanila","choclate","pineapple"]
for flavor in flavors:
    print(f"flavors:{flavor} , lenght:{len(flavor)}")
total_L = sum(len( flavor ) for flavor in flavors)
average_L = total_L / len(flavors) if flavors else 0
print(f"average lenght of flavors : , {average_L}") 


#Store all the ice cream flavors in a list. Sort the list alphabetically and print the sorted flavors



flavors=["vanila","choclate","pineapple"]
flavors.sort()
print("sorted list of flavor")
for flavor in flavors:
    print (flavor) 


#Create a dictionary where keys are the topping names and values are their respective prices. 
#Calculate the total cost if a customer selects three toppings: Chocolate Chips, Whipped Cream, and Gummy Bears.

topping_names = {"Chocolate Chips" : 2.5 ,
                  "Whipped Cream" : 1.5 ,
                   "Gummy Bears" : 1,
                   "blueberry" : 4  }
selected_toppings = ("Chocolate Chips" ,"Whipped Cream" , "Gummy Bears" )
total_cost = sum (topping_names[toppings] for toppings in selected_toppings)
print(f"total cost for the selected groups is: {total_cost}")


#Convert the suggested price list for "base ice creams" into a tuple. Print the most expensive and least expensive options.

base_icecreams =  ((3.5, "Vanilla"),
(4.0, "Chocolate"),
(3.8, "Strawberry"),
(4.2, "Mint"),
(4.5, "Cookies and Cream")
)
sorted_prices = sorted(base_icecreams)
least_expensive = sorted_prices[0]
most_expensive = sorted_prices[-1]

print(f"the least expensive ice cream is : {least_expensive}")
print(f"the most expensive ice cream is : {most_expensive}")





# Write a program to determine if an ice cream flavor is classified as "classic," "trendy," or "kid-friendly" based on the flavor name input.

flavor = input("the ice cream flavor is classified as : ")
if flavor in ["vanilla" , "blueberry" , "strawberry"]:
    print("{flavor} is a classic color")
elif flavor in ["cream" , "choclate" , "caramelblue"]:
    print(f"{flavor} is a trendy color")
elif flavor in ["dryfruit" , "oreocream" , "pineapple"]:
    print(f"{flavor} is a kid-friendly")
else:
    print(" invalid ")   


#7Check if a given city (input by the user) is in the list of suggested cities for the business. 
# Print "Valid city" if found; otherwise, print "Invalid city."

city = input("name of the given city is :")
if city in {"florida" , "miami" , "kansas-city" , "saint-louis" , "olathe" , "belton" , "grandview" , "lenexa"}:
    print(f"{city} valid city")
else:
    print("Invalid city") 

#8Iterate through all suggested topping combinations and print them with their respective total prices. 
# For example: Vanilla + Chocolate

topping_prices = {"chocolate chips" : 1.5  ,
                  "sprinkels" : 1.2  ,
                  "oreo-chips" : 1.0,
                  "dry-nuts ": 1.3}
baseings = {"vanilla" , "chocalte" , "blueberry"}
for base in baseings:
    for topping , price in topping_prices.items() :
        total_price = price
print(f"{base} + {topping} : ${total_price:.2f}") 