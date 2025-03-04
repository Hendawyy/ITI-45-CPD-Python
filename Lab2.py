# 1. Reverse a String
# Write a Python program to reverse a string.
# ========================================================
# q1=input("Please input a string: ")
# print(q1[::-1])


# ========================================================
# 2. Check if a String is a Palindrome
# Write a Python program to check if a string is a palindrome (reads the same backward as forward).
# ========================================================
# q2=input("Please Input a strint to check if Palindrome: ")
# print(q2==q2[::-1])


# ==================================================Ah======
# 3.Remove Duplicates from a String
# Write a Python program to remove duplicate characters from a string.
# #Output=
# ========================================================
# q3=input("Please Enter A String To remove duplicates: ")
# nd=set(q3.lower())
# print(f"Output={''.join(nd)}")

# =========================================================
# 4.Find the Longest Word in a String
# Write a Python program to find the longest word in a given string.
# text = "Python is a great programming language"
#Output=programming
# ========================================================
# text = "Python is a great programming language"
# print(max(text.split(" "), key=len))


# ========================================================
# 5.Find Common Elements Between Two Tuples
# Write a Python program to find common elements between two tuples.
# ``` python
# tuple1 = (1, 2, 3)
# tuple2 = (2, 3, 4)
# ========================================================
# tuple1 = (1, 2, 3)
# tuple2 = (2, 3, 4)
# print(tuple(set(tuple1).intersection(tuple2)))


# ========================================================
# 6.Find the Maximum and Minimum Value in a Dictionary
# Write a Python program to find the maximum and minimum value in a dictionary.
# my_dict = {"a": 10, "b": 20, "c": 5} 
# Min= 5  , max=20
# ========================================================
# my_dict = {"a": 10, "b": 20, "c": 5}
# print(f"Min={min(my_dict.values())}, Max={max(my_dict.values())}")
# ========================================================


# 7- Merge Two Dictionaries
# Write a Python program to merge two dictionaries.
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# ========================================================
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# dict1.update(dict2)
# print(f"Output: {dict1}")
# ========================================================


# 8- Find Common Keys in Two Dictionaries
# Write a Python program to find common keys in two dictionaries.
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 2, "c": 4, "d": 5}
# #Output: {'b', 'c'}
# ========================================================
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 2, "c": 4, "d": 5}
# print(set(dict1).intersection(dict2))
# ========================================================


# 9- takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu
# ========================================================

string="abdulrahman"
longest = string[0]
ls=[]

for i in range(1, len(string)):
    if string[i] > string[i-1]:
        longest+=string[i]
    else:
        ls.append(longest)
        longest = string[i]
        
ls.append(longest)
print(ls)
print(max(ls,key=len))
# ========================================================