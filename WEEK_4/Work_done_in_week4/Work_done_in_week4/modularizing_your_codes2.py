### **3. Python Modules
# **Different Ways to Import Modules**

# 1. Import the whole module
import math
# Lets put it to use
print(math.sqrt(9))      # Output will be 3 because square root of 9 is 3.
# - Note that you must specify the module name when calling a function within it.


# 2. import as an alias
import math as m
# lets put it to use
print(m.sqrt(25))         # Output will be 5 because root of 25 is 5.
# - This shortens the module name, this is common with libraries like numpy, pandas, etc


# 3. Import specific functions or variables
from math import sqrt, pi
print(sqrt(36))       # Output is 6
print(pi)             # pi is 3.142
# - here you dont need the prefix 'math.' anymore


# 4. Import everything from the module
from math import *
print(sqrt(49))
print(pi)
# - This is usually not recommended because it can cause name conflits if two modules have functions with the same name


### **4. Python Packages**




