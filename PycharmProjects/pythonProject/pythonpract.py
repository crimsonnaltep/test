"""LOOPS"""

# 1. Write a program to loop through a range from 0 to 100 and print the even numbers only.
# for i in range(101):
#     if i%2==0:
#         print(i)
# 2. Write a program to loop through a range from 350 to 677 and print only numbers ending with 7.
# for i in range(350, 678):
#     if i % 10 == 7:
#         print(i)
# 3. Print every 6th number from 0 to 100.
# for i in range(0, 101, 6):
#     print(i)
# 4. Write a program that will output the multiplication table.
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i*j}")
#     print("\n")
# 5. Write the FizzBuzz program. Only this time, loop through a range of 0-100 and for each iteration, print Fizz,
# if the loop variable is divisible by 3, Buzz, if it's divisible by 5, and FizzBuzz if it's divisible by both.
# for i in range(101):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
# 6. Write a program that will loop through a range of 0-1000 and print out only prime numbers.
# for i in range(1001):
#     count = 0
#     for j in range(2, 1000):
#         if i % j == 0:
#             count += 1
#     if count == 1:
#         print(i)
# 7. Write a program that will keep a random number from 1-10 (use random package). The user must guess that number.
# They can input as many times as they want. Terminate the program with a congratulation message when the user has
# guessed the number.
#
# import random
# n = random.randint(1,10)
# flag = True
# lives = 3
# while flag:
#     if lives == 0:
#         print("Better luck next time")
#         break
#     g = int(input("Enter the number: "))
#     if n == g:
#         print("Great job c; <зз")
#         flag = False
#     else:
#         if g < n:
#             print("Take a little bit higher mate")
#         elif n < g:
#             print("Take a little bit lower bro")
#         lives -= 1
#         continue

# To make this more interesting, you can add lives (attempt limit) for the user, and after each guess let them know if
# their guess was larger or smaller from the actual number.
# import random
# n = random.randint(1,100)
# flag = True
# while flag:
#     g = int(input("Enter the number: "))
#     if n == g:
#         print("Great job c; <зз")
#         flag = False
# Գրել խաղ, որը կպահի 1-100 պատահական թիվ։ Խաղացողը պետք է գուշակի այդ թիվը։ Նա կարող է այնքան անգամ գուշակել, ինչքան
# ցանկանում է։ Ավարտել ծրագիրը շնորհավորանքի նամակ տպելով, երբ խաղացողը թիվը գուշակի։

# Խաղն ավելի հետաքրքիր դարձնելու համար կարելի է սահմանափակել հնարավորությունների քանակը։ Կարելի է նաև խաղացողին
# տեղեկացնել, արդյո՞ք նրա մուտքագրած թիվը մեծ է պահված թվից, թե փոքր։

"""Bonus"""

# 8. Given a string, print a string where for every character in the original, there are two characters.
# Տրված է սթրինգ։ Տպեք նոր սթրինգ, որը կպարունակի օրիգինալ սթրինգի բոլոր տառերը կրկնապատկված։

# Օրինակ, եթե ունենք հետևյալ սթրինգը՝ Monty, պետք է ստանանք MMoonnttyy
# s = input()
# for i in s:
#     print(i*2, end = "")
# 9. Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So
# "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
# s1 = input()
# s2 = input()
# yi = 0
# for i in range(min(len(s1) - 1, len(s2) - 1)):
#     if s1[i] + s1[i + 1] == s2[i] + s2[i + 1]:
#         yi += 1
# print(yi)
# 10. Reverse a string without the use of indexation (e.g. [::-1]).
# Շրջել սթրինգը առանց գործածելու str[::-1]
# s = input()
# i = len(s)-1
# while i >= 0:
#     print(s[i], end = "")
#     i -= 1
