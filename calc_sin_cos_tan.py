# Assignment 7)
# You need to design a calculator for the formulaes/functions below:
# sin(x), cos(x), tan(x),log(x)
# If i enter 'a'/invalid characters it should throw meaningful error.
# for valid numbers it should display in a fromat like below:
# ------------------------
# Sin Value: Result
# -------------------------
# Cos Value: Result
# -------------------------
# Tan Value Result

import math
a= eval(input ("Enter degree from 0 to 360 to get sin, cos, tan, log values: "))
print(a)
print("---------------------------")
sine_a = round(math.sin(math.radians(a)),1) # rounded to single precision
print("Sine value of", a,"is", sine_a)
print("---------------------------")
cos_a = round(math.cos(math.radians(a)),1) # rounded to single precision
print("cosine value of", a,"is", cos_a)
print("---------------------------")
tan_a = round(math.tan(math.radians(a)),1) # rounded to single precision
print("Tan value of", a,"is", tan_a)
print("---------------------------")
log_a = round(math.log(math.radians(a)),1) # rounded to single precision
print("log value of", a,"is", log_a)
print("---------------------------")
