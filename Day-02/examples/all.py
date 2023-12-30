div = "*****************************"
# String concat
str1 = "Hello"
str2 = "world"
print(str1+" "+str2)
print(div)

# length 
length = "Hi I am Akshay Deshpande"
print("Length of string "+length + " is : " , len(length))
print(div)

# lower and upper case
strCase = "Akshay deshpande"
print("Upper : "+strCase.upper())
print("Lower : "+strCase.lower())
print(div)

# Replace
strRpl = "Python is awesome"
print("Original String :"+strRpl+"\nReplaced String :"+strRpl.replace("awesome","greate"))
print(div)

# Split
strSpl = "Python is awesome"
print("Words",strSpl.split())
print(div)

# Strip
strStrip = "   Some Spaces arround  "
print("Stripped text :"+strStrip.strip())
print(div)

# SubString
strSubStr = "Python is awesom"
subStr = "is"
if strSubStr in strSubStr:
    print(subStr+" is found in text")
print(div)    

# Float variables
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)
print(div)

# Integer variables
num1 = 12
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)
print(div)

# regex find all
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
print(div)

# Regex match
text = "The quick brown fox"
pattern = r"The quick brown fox"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
print(div)

# Regex replace
text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
print(div)

#Split
text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)