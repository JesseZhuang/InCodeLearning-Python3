# provides access to the mathematical functions defined by the C standard.
# These functions cannot be used with complex numbers;
# use the functions of the same name from the cmath module.
# Except when explicitly noted otherwise, all return values are **floats**.

# In[1]:

import math

dir(math)

# --------
# __*round() vs math.ceil() vs math.floor()*__

# In[3]:

print(round(2.1))
print(round(2.8))
print("-" * 20)
print(math.ceil(2.1))
print(math.ceil(2.8))
print("-" * 20)
print(math.floor(2.1))
print(math.floor(2.8))

# math.fmod(x, y)
# Note that the Python expression x % y may not return the same result.
# The intent of the C standard is that fmod(x, y) be exactly (mathematically;
# to infinite precision) equal to x - n*y for some integer n such that the
# result has the __same sign as x and magnitude less than abs(y)__. __Python’s
# x % y returns a result with the sign of y instead__, and may not be exactly
# computable for float arguments. For example, fmod(-1e-100, 1e100) is -1e-100,
# but the result of Python’s -1e-100 % 1e100 is 1e100-1e-100, which cannot be
# represented exactly as a float, and rounds to the surprising 1e100. For this
# reason, function fmod() is generally preferred when working with floats,
# while Python’s x % y is preferred when working with integers.

# In[4]:

print(math.fmod(7, 2))
print(7 % 2)

# In[6]:

print(math.fmod(7, -2))
print(7 % (-2))

# *Comments: In JavaScript, 7 % (-2) is also 1.*

# --------
# __*sum() vs math.fsum()*__
# > Return an accurate floating point sum of values in the iterable. Avoids
# loss of precision by tracking multiple intermediate partial sums.

# In[7]:

print(sum([0.1 for i in range(10)]))
print(math.fsum([0.1 for i in range(10)]))

# --------
# _math.gcd(a, b)_
# > Return the greatest common divisor of the integers a and b. If either
# a or b is nonzero, then the value of gcd(a, b) is the largest positive int
# that divides both a and b. gcd(0, 0) returns 0.

# In[8]:

math.gcd(25, 20)

# --------
# __*math.isfinite(), math.isinf(), math.isnan()*__

# In[13]:

math.isfinite(math.inf)

# In[14]:

math.isinf(math.inf)

# In[15]:

math.isnan(math.nan)

# ---------
# __*math.modf() and math.trunc()*__

# In[17]:

math.modf(3.1415)

# In[16]:

math.trunc(3.1415)

# > For the ceil(), floor(), and modf() functions, note that all floating-point
# numbers of sufficiently large magnitude are exact integers. Python floats
# typically carry no more than 53 bits of precision (the same as the platform
# C double type), in which case any float x with abs(x) >= 2**52 necessarily
# has no fractional bits.

# ------
# __*Power and logarithmic functions*__
# math.exp(x)
# > Return e**x.
# math.expm1(x)
# > Return e**x - 1.
# math.log(x[, base])¶
# >With one argument, return the natural logarithm of x (to base e).
# >With two arguments, return the logarithm of x to the given base, calculated
# as log(x)/log(base).
# math.log2(x)
# > Return the base-2 logarithm of x. This is usually more accurate than
# log(x, 2).
# math.log10(x)
# > Return the base-10 logarithm of x. This is usually more accurate than
# log(x, 10).

# math.pow(x, y)
# > Return x raised to the power y.
# > Unlike the built-in \*\* operator, math.pow() converts both its arguments
#  to type float. Use \*\* or the built-in pow() function for computing exact
#  integer powers.

# math.sqrt(x)
# > Return the square root of x.

# -------
# __*Constants*__

# math.pi
# > The mathematical constant π = 3.141592..., to available precision.

# math.e
# > The mathematical constant e = 2.718281..., to available precision.

# math.inf
# > A floating-point positive infinity. (For negative infinity, use -math.inf.)
# Equivalent to the output of float('inf').
# math.nan
# > A floating-point “not a number” (NaN) value. Equivalent to the output of
# float('nan').

# In[18]:

1 / math.inf

# --------
# #### Unicode and UTF-8
# > UTF-8就是在互联网上使用最广的一种Unicode的实现方式。其他实现方式还包括UTF-16
# （字符用两个字节或四个字节表示）和UTF-32（字符用四个字节表示），不过在互联网上基本不用
# 重复一遍，这里的关系是，UTF-8是Unicode的实现方式之一。
# UTF-8最大的一个特点，就是它是一种变长的编码方式。它可以使用1~4个字节表示一个符号，
# 根据不同的符号而变化字节长度。
# UTF-8的编码规则很简单，只有二条：
# 1）对于单字节的符号，字节的第一位设为0，后面7位为这个符号的unicode码。因此对于英语字母，
# UTF-8编码和ASCII码是相同的。
# 2）对于n字节的符号（n>1），第一个字节的前n位都设为1，第n+1位设为0，
# 后面字节的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的unicode码。

# | Unicode符号范围 (十六进制) | UTF-8编码方式 (二进制) |
# | :-------------|:-------------|
# | 0000 0000-0000 007F | 0xxxxxxx |
# | 0000 0080-0000 07FF | 110xxxxx 10xxxxxx |
# | 0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx |
# | 0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

# > 根据上表，解读UTF-8编码非常简单。如果一个字节的第一位是0，则这个字节单独就是一个字符；
# 如果第一位是1，则连续有多少个1，就表示当前字符占用多少个字节。
# Ref: http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html
