# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio' ]
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class = (class_1 + class_2)
print (new_class)


# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)


# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)

# Code ends here


# --------------
# Code starts here
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
#
math=courses['Math']
english=courses['English']
history=courses['History']
french=courses['French']
science=courses['Science']

#
total = math + english + history + french + science
#
print (total)
#
percentage = (total * 100 / 500)
#
print(percentage)



# Code ends here


# --------------
# Code starts here




mathematics={'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75 }
max_marks_scored = max(mathematics,key = mathematics.get)
print(max_marks_scored)
topper=max_marks_scored
print(topper)



# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
A= topper.split()
print(A)
last_name='ng'
first_name='andrew'
full_name= last_name + ' ' + first_name
print(full_name)
certificate_name= full_name.upper()
print(certificate_name)

# Code starts here



# Code ends here


