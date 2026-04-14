#operatios on string(immutable)
a='a!!harrY!!!! !!!!harry harry!!!!!'
print(len(a))
print(a.upper())#strings are immutable and when we upper it it creates a new string 
print(a.lower())#lowers 
print(a.rstrip('!'))#removes ! from rhs 
print(a.lstrip('!'))
print(a.replace('harry','john'))
print(a.split(' '))#creates a list from string having space in between
print(a.capitalize())#capitalize first alphabet to capital and rest to small
str1='Welcome to python'
print(len(str1))
print(str1.center(50))#centralise with spacesz
print(len(str1.center(50)))
print(a.count('harry'))#prints number of word coming in string 
print(a.endswith('!!!!!!'))
print(str1.endswith('to',4,10))#chcecking 4:10 and to ends 
print(str1.find('hi'))#returns -1 if not found 
print(str1.index('W'))#returns index positing of te particular number entered 
print(str1.isalnum())#checks for alphabets 
print(str1.isalpha())
print(str1.islower())#checks for lower returns false if any thing is capital
print(str1.isprintable())#checks if all characters are prinatale 
print(str1.isspace())#checks for wide space
print(str1.istitle())#check for first letter of EACH word
print(str1.startswith('Welcome'))#checks for starts with 
print(str1.swapcase())#converts upper to lower and lower to upper
print(str1.title())#coverts first letter to capital