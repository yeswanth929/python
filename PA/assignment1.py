#1find even or odd

number=int(input("Given number is : "))
if(number % 2 == 0):
 print("The number is even")
else:
 print("The number is odd")

#2Write a program that takes a number from the user and prints:
#"Positive" if the number is greater than zero.
#"Negative" if the number is less than zero.
#"Zero" if the number is exactly zero.

number = int(input("given number is: "))

if(number > 0):
   print(" Positive! ")
elif(number < 0):
   print(" Negative! ")
else:
    print(" Zero! ")




#3Write a program to check if a given year is a leap year. A year is a leap year if:
#It is divisible by 4, and
#Not divisible by 100 unless it is also divisible by 400.



year = int(input("given number is : "))
if(year % 400 == 0):
  print("year is leap year")
elif(year % 100 == 0):
  print("year is not leap year")
elif(year % 4 == 0):
  print("year is leap year")
else:
  print("year is not aleap year")



#4Write a program that takes three numbers from the user and prints the largest of the three.

n1=int(input("given number n1 is: "))
n2=int(input("given number n2 is: "))
n3=int(input("given number n3 is: "))
if(n1 > n2 and n1 > n3):
  print("the greatest number is: " ,n1 )
elif(n2 > n3 and n2 > n1):
  print("the greatest number is: " ,n2 )
elif(n3 > n1 and n3 > n2):
  print("the greatest number is: " ,n3 )
else:
  print("invalid!")

  
#5Write a program that takes a score (0 to 100) from the user and assigns a grade:
  
# 90-100: Grade A 
# 80-89: Grade B
# 70-79: Grade C
# 60-69: Grade D  90 <= m <= 100:
# Below 60: Grade F

m= int(input("marks scored by the student is: "))
if(90 <= m and m <= 100  ):
  print("Grade A")
elif(80 <= m and m <= 89 ):
  print("Grade B")
elif(70 <= m and m <= 79 ):
  print("Grade C")
elif(60 <= m and m <= 69 ):
  print("Grade D")
else:
   print("Grade F")


#6Write a program that checks if a given character is a vowel (a, e, i, o, u) or a consonant. Assume the input is a single letter.


letter= input("given letter : ").lower()
if letter in {'a','e','i','o','u'}:
  print("vowel")
else:
  print("consonant") 


#7Write a program that checks if a number is within a specific range. Ask the user to input the number, as well as the start and end of the range. 
#Print "In range" if the number is within the range, otherwise print "Out of range".

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

n1= int(input("give number : "))

if (start<= n1 <= end):
  print("in range")
else:
  print("out of range") 


#8Write a program that takes two numbers and checks if the first number is divisible by the second. If not, print the remainder.


n1 = int(input("give the first number: "))
n2 = int(input("give the second number: "))

if (n1 % n2 == 0):
  print("1st number is divisible by 2nd")
else:
  remainder = n1 % n2
  print(f"The remainder is {remainder}") 


#9Write a program that asks for the user’s age and checks if they are eligible to vote. Assume the voting age is 18 or older

age=int(input("the person age is "))
if (age >=18):
  print("eligible to vote")
else:
  print("not eligible to vote your age is not 18 or above") 


#10Write a program that takes three numbers from the user and prints the smallest of the three.
n1 = int(input("give the 1st number: "))
n2 = int(input("give the 2nd number: "))
n3 = int(input("give the 3rd number: "))
if ( n1 <= n2 and n1 <= n3 ):
    print(f"{n1} is the smallest")
elif( n2 <= n1 and n2 <= n3 ):
    print(f"{n2} is the smallest")
elif(n3 <= n1 and n3 <= n2):
    print(f"{n3} is the smallest")
else:
    print("invalid!")
