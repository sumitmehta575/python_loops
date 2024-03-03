#1.Print number from 1 to 5 using a while loop.
n=6
i=1
while i<n:
    print(i)
    i=i+1

#2.Calclate the sum of number from 1 to 10 using a while loop.
sum = 0
num = 1
while num <= 10:
    sum += num
    num += 1
    print ("the sum of numbers from 1 to 10 is:",sum)

#3.Calclate the factorial of a number using a for loop.
n=5
fact = 1
for i in range (1,n+1):
    fact *= i
    print ("factorial=",fact)

#4.Count the number of vowel in a string using a for loop.
def count_vowels(string):
    vowel_count = 0
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count
input_string = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(input_string))

#5.Print a pattern using nested loop.
row = 1
while row <= 5 :
    col = 1
    while col <= row :
        print ("*" , end = "")
        col=col+1
    print()
    row = row +1

#6.Generate a mltiplication table using nested loop.
n =int(input("enter no:"))
for i in range (1,11):
    print(n*i)