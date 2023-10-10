"""Regular expression
https://docs.python.org/3/howto/regex.html
Regular expressions (called REs, or regexes, or regex patterns)
are essentially a tiny, highly specialized programming language
embedded inside Python and made available through the re module.
Using this little language, you specify the rules for the set
of possible strings that you want to match

http://www.ucs.cam.ac.uk
A regular expression is simply some means to write down a pattern
describing some text.

LP1: ^    \A    matches the beginning of a string
     $    \Z    matches the end of a string
LP2: \b    matches a word boundary
LP3: \d    matches any numeric digit
     \D    matches any non-numeric character
     \s    matches any white space character (space, tab, ...)
     \S    matches any non-white space character
     \w    [0-9a-zA-Z_]    matches any "word character"
     \W    [^0-9a-zA-Z_]   matches any non-word character
LP6: x?    matches an optional x character
     x*    matches x zero or more times
     x+    matches x one or more times
     x{n, m}    matches an x character at least n times, not more than m times
LP7: (a|b|c)    matches either a or b or c
LP8: (x) in general is a remembered group.

http://www.pyregex.com/
"""


import re


# 1. simple testing example w/o regular exp
print("*********** Matching w/o Regex    ************")

S = "Regular expressions easily explained"
_yn = "easily" in S

print(_yn)

# 2. Simple Regex

print("*********** Simple RegEx           ************")
x = re.search("cat", "A cat and a rat can't be friend.")
print(x)

x = re.search("cow", "A cat and a rat can't be friend.")
print(x)

x = re.match("cat", "A cat and a rat can't be friend.")
print(x)

# will match from start of string
print(re.match("A cat", "A cat and a rat can't be friend."))

# 3. Combine If logic
print("*********** If RegEx                ************")
if re.search("cat", "A cat and a rat can't be friend."):
    print('Find the "cat"')
else:
    print('Can\'t find the "cat"')

if re.search("cow", "A cat and a rat can't be friend."):
    print('Find the "cat"')
else:
    print('Can\'t find the "cow"')

# 4. Raw format r"

print("*********** User Raw format         ************")
if re.search(r"is", "Mayer is a very common Name"):
    print('Find the "is"')
else:
    print('Can\'t find the "is"')

# 5. Add patterns
print("*********** User Pattern parameters ************")
if re.search(r"M[ae][iy]er", "Mayer is a very common Name"):
    print('Find the Match')
else:
    print('Can\'t find the Match')

# 6. Add param -I ignore case
print("*********** Add parameters ************")
if re.search(r"mayer", "Mayer is a very common Name\n"):
    print('Find the Mayer')
elif re.search(r"mayer", "Mayer is a very common Name\n", re.I):
    print('Find the Mayer with case insensitive')
else:
    print('Can\'t find the Mayer')

# 7. Grouping and back reference

mo = re.search("([0-9]+).*: (.*)", "Customer number: 2454, Date: Feb 12, 2011")
print("*********** back reference ************")
print("Back reference .group():", mo.group())  # 2454, Date: Feb 12, 2011
print("Back reference .group(0):", mo.group(0))  # 2454, Date: Feb 12, 2011
print("Back reference group(1):", mo.group(1))  # 2454
print("Back reference group(2):", mo.group(2))  # Feb 12, 2011


print(re.search('[^aeiou]y$', 'vacancy'))
# not raise error

print(re.sub('([^aeiou])y$', r'\1ies', 'vacancy'))
# ([^aeiou])y$ the word that ends with not aeiou + y
# \1 group 1; group 0 is the whole content
# raise error if there is no parenthesis in .sub method, () forms group
