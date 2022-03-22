

'''
Regular Expression:Regex
It is a sequence of character that is used to defined a search pattern.

1) Form Validation
2) Data cleaning-search and replace.

For regular express 're' module is used.
Following methods from the re modules are used in regular expression.
1) finadall()
2) split()
3) sub()
4) search()
'''

import re



str="Data Manipulation is done in Data science, Data in the Database is important"

res=re.findall('Data',str)#returns list
print(res)