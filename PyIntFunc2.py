'''
# 1. Update Values in Dictionaries and Lists

   A. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
   B. Change the last_name of the first student from 'Jordan' to 'Bryant'
   C. In the sports_directory, change 'Messi' to 'Andres'
   D. Change the value 20 in z to 30
'''
# Code supplied for exercise:
x = [ [5,2,3], [10,8,9] ] 
students = [
   {'first_name':  'Michael', 'last_name' : 'Jordan'},
   {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
   'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
   'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# my code:
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30




'''
#2 Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
the function loops through each dictionary in the list and prints each key and the 
associated value. For example, given the following list:
'''
students = [
   {'first_name' : 'Michael', 'last_name' : 'Jordan'},
   {'first_name' : 'John', 'last_name' : 'Rosales'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
'''
iterateDictionary(students) 
should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''
def iterateDictionary(some_list):
   for x in range(len(some_list)):
      print(some_list[x])

# iterateDictionary(students)

def formatDictionary(some_list):
   for e in some_list:
      for x,y in e.items():
         print(f"{x} - {y}")

# test:
# formatDictionary(students)




'''
#3 Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries 
and a key name, the function prints the value stored in that key for each dictionary. 
'''
def iterateDictionary2(key_name, some_list):
   for e in some_list:
      print(e[key_name])

# test:
# iterateDictionary2('first_name', students)




'''
#4 Create a function printInfo(some_dict) that, given a dictionary whose values are all lists, prints the 
name of each key along with the size of its list, and then prints the associated values within each key's list.
'''
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
   for e in some_dict:
      print(len(some_dict[e]), e)
      print(some_dict[e])

# test:
# printInfo(dojo)